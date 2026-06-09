from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import numpy as np
import xarray as xr

if TYPE_CHECKING:
    import os
    from typing import Any, Protocol

    import numpy.typing as npt

    class FileLike(Protocol): ...

    class LockType(Protocol):
        def __enter__(self) -> Any: ...

        def acquire(self, blocking: bool = True, timeout: int = -1) -> bool: ...
        def release(self) -> None: ...

    IndexerType = int | slice | npt.NDArray[np.integer]
    FilenameOrObjectType = str | os.PathLike | bytes | FileLike


@dataclass
class ImageIOBackendArray(xr.backends.BackendArray):
    filename_or_obj: FilenameOrObjectType

    shape: tuple[int]
    dtype: npt.DtypeLike

    lock: LockType

    def __getitem__(self, key: tuple[IndexerType]):
        return xr.core.indexing.explicit_indexing_adapter(
            key,
            self.shape,
            xr.core.indexing.IndexingSupport.BASIC,
            self.basic_indexing,
        )

    def basic_indexing(self, key: tuple[IndexerType]) -> npt.NDArray:
        import imageio.v3 as iio

        with self.lock, iio.imopen(self.filename_or_obj, io_mode='r') as f:
            if key == (slice(None),) * len(self.shape):
                return f.read()

            first_indexer = key[0]
            if isinstance(first_indexer, int):
                data = f.read(index=first_indexer, mode='P', writable=True)

                remaining_indexers = key[1:]
            else:
                if isinstance(first_indexer, slice):
                    indices = range(*first_indexer.indices(self.shape[0]))
                else:
                    indices = first_indexer

                data = np.concatenate([f.read(index=index, mode='P') for index in indices], axis=0)

                remaining_indexers = (..., *key[1:])

            return data[remaining_indexers]


class ImageIOBackend(xr.backends.BackendEntrypoint):
    def open_dataset(
        self, filename_or_obj: FilenameOrObjectType, *, drop_variables: bool | None = None
    ) -> xr.Dataset:
        import imageio.v3 as iio

        with iio.imopen(filename_or_obj, io_mode='r') as f:
            properties = f.properties()
            metadata = f.metadata()

            dims = ['n_images', 'height', 'width', 'color']

            background = metadata['background']
            duration = metadata['duration']

            shape = properties.shape
            dtype = properties.dtype

        backend_array = ImageIOBackendArray(
            filename_or_obj=filename_or_obj,
            shape=shape,
            dtype=dtype,
            lock=xr.backends.locks.SerializableLock(),
        )
        data = xr.core.indexing.LazilyIndexedArray(backend_array)

        var = xr.Variable(
            dims=dims,
            data=data,
            attrs={'duration': duration, 'background': background},
            encoding={'preferred_chunks': dict(zip(dims, (1, *shape[1:])))},
        )

        return xr.Dataset({'data': var}, coords={'color': ['red', 'green', 'blue']})
