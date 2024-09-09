# Reading data using backends

## Introduction

You can [read different types of files](https://docs.xarray.dev/en/stable/user-guide/io.html) in `xr.open_dataset` by specifying the engine to be used:

```python
import xarray as xr
xr.open_dataset("my_file.grib" , engine="cfgrib")
```

Navigating Xarray backends can be confusing,
so we recommend checking out [this flow chart](https://docs.xarray.dev/en/stable/user-guide/io.html)
to help you figure out which engine you need and how to use it.

You can see what backends are currently available in your working environment
with `xarray.backends.list_engines()`.

## Why use the Xarray backend API to write your own backend?

- Your users don't need to learn a new interface; they can use `xr.open_dataset` with the `engine` kwarg.
- With little extra effort you can have lazy loading with Dask. Simply implement a function for reading blocks and Xarray will manage lazy loading with Dask for you.
- It's easy to implement: using the backend API (introduced in v0.18.0), you don't need to integrate any code in Xarray.

## More Information

See the [documentation](https://docs.xarray.dev/en/stable/internals/how-to-add-new-backend.html) for more details on adding and registering a new backend.

Follow the tutorials on creating a new backend for binary files.

```{tableofcontents}

```

### Links to internal backends

- [netcdf4](https://pypi.org/project/netCDF4/) - netCDF4
- [scipy](https://scipy.org/) - netCDF3
- [zarr](https://pypi.org/project/zarr/) - Zarr
- [pydap](https://pydap.github.io/pydap/) - Data Access Protocol (DAP/DODS/OPeNDAP)
- [h5netcdf](https://h5netcdf.org/) - hdf5

### Links to external backends (not comprehensive)

- [cfgrib](https://github.com/ecmwf/cfgrib) - GRIB
- [tiledb](https://github.com/TileDB-Inc/TileDB-CF-Py) - TileDB
- [rioxarray](https://corteva.github.io/rioxarray/stable/) - GeoTIFF, JPEG-2000, ESRI-hdr, etc (via GDAL)
- [xarray-sentinel](https://github.com/bopen/xarray-sentinel) - Sentinel-1 SAFE
- ...
