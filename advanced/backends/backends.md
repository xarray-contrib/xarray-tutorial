# Reading data using backends

## Introduction

You can [read different types of files](https://docs.xarray.dev/en/stable/user-guide/io.html) in `xr.open_dataset` by specifying the engine to be used:

```python
import xarray as xr
xr.open_dataset("my_file.grib" , engine="cfgrib")
```

The "engine" provides a set of instructions that tells xarray how to read the data and pack them into a `dataset` (or `dataarray`).
These instructions are stored in an underlying "backend".

Xarray comes with several backends that cover many common data formats.
Many more backends are available via external libraries, or you can write your own.
This diagram aims to help you determine - based on the format of the file you'd like to read -
which type of backend you're using and how to use it.
The rectangular boxes are clickable with more information.

```{mermaid}
---
title: "Xarray Engines: Opening Your Data with xr.open_dataset()"
---


flowchart TD
    built-in-eng[Is your data stored in one of these formats?
        netCDF4 (**netcdf4**)
        netCDF3 (**scipy**)
        Zarr (**zarr**)
        DODS/OPeNDAP (**pydap**)
        HDF5 (**h5netcdf**)
        ]

    built-in("`You're in luck! Xarray bundles a backend for this format.
        Open data using *xr.open_dataset()*. We recommend
        always setting the engine you want to use.`")

    installed-eng["`One of these formats (this list is not inclusive)?
        GRIB (**cfgrib**)
        TileDB (**tiledb**)
        GeoTIFF, JPEG-2000, ESRI-hdf (**rioxarray**, via GDAL)
        Sentinel-1 SAFE (**xarray-sentinel**)
        ...
        `"]

    installed("`Install the package indicated in parentheses
        to your Python environment. Restart the kernel
        and use *xr.open_dataset(files, engine='rioxarray')*`")

    other("`Ask around to see if someone in your data community
        has created an Xarray backend for your data type.
        If not, you may need to create your own or consider
        exporting your data to a more common format.`")

    built-in-eng -->|Yes| built-in
    built-in-eng -->|No| installed-eng

    installed-eng -->|Yes| installed
    installed-eng -->|No| other

    click built-in-eng "https://docs.xarray.dev/en/stable/getting-started-guide/faq.html#how-do-i-open-format-x-file-as-an-xarray-dataset"
    click installed-eng "https://corteva.github.io/rioxarray/stable/getting_started/getting_started.html#rioxarray"
    click other "https://docs.xarray.dev/en/stable/internals/how-to-add-new-backend.html"

    classDef quesNodefmt fill:#9DEEF4,stroke:#206C89
    class built-in-eng,installed-eng quesNodefmt

    classDef ansNodefmt fill:#FFAA05,stroke:#E37F17
    class built-in,installed,other ansNodefmt

    linkStyle default font-size:20pt,color:#206C89

```

## Why use the Xarray backend API?

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
- [scipy]https://scipy.org/) - netCDF3
- [zarr](https://pypi.org/project/zarr/) - Zarr
- [pydap](https://pydap.github.io/pydap/) - Data Access Protocol (DAP/DODS/OPeNDAP)

### Links to external backends (not comprehensive)

- [cfgrib](https://github.com/ecmwf/cfgrib) - GRIB
- [tiledb](https://github.com/TileDB-Inc/TileDB-CF-Py) - TileDB
- [rioxarray](https://corteva.github.io/rioxarray/stable/) - GeoTIFF, JPEG-2000, ESRI-hdr, etc (via GDAL)
- [xarray-sentinel](https://github.com/bopen/xarray-sentinel) - Sentinel-1 SAFE
- ...
