# Creating new backends

## Introduction

```mermaid
---
title: "Xarray Engines: Opening Your Data with xr.open_dataset()"
---


flowchart TD
    built-in-eng([Is your data stored in one of these formats?
        netCDF4
        netCDF3
        Zarr
        DAP
        ])

    built-in("`You're in luck! Xarray bundles a backend for this format.
        Open data using *xr.open_dataset()* as normal.`")

    installed-eng(["`One of these formats?
        GRIB (**cfgrib**)
        TileDB (**tiledb**)
        GeoTIFF, JPEG-2000, ESRI-hdf (**rioxarray**, via GDAL)
        Sentinel-1 SAFE (**xarray-sentinel**)
        `"])

    installed("`Install the package indicated in parentheses
        to your Python environment. Restart the kernel
        and use *xr.open_dataset(files, engine='rioxarray')*`")

    other("`You can't use *open_dataset()* with an engine.
        This page shows how to open your data with Xarray.`")

    built-in-eng -->|Yes| built-in
    built-in-eng -->|No| installed-eng

    installed-eng -->|Yes| installed
    installed-eng -->|No| other

    click built-in-eng "https://tutorial.xarray.dev/advanced/backends/backends.html"
    click installed-eng "https://tutorial.xarray.dev/advanced/backends/backends.html#why-using-the-xarray-backend-api"

```

You can [read different type of files](https://docs.xarray.dev/en/stable/user-guide/io.html) in `xr.open_dataset` by specifying the engine to be used:

```python
import xarray as xr
xr.open_dataset("my_file.grib" , engine="cfgrib")
```

For each available engine there is an underlying backend, that reads the data and pack them in a dataset.

Xarray bundles several backends internally for the following formats:

- netcdf4 - netCDF4
- scipy - netCDF3
- zarr - Zarr
- pydap - DAP
- ...

External Backends that use the new backend API (xarray >= v0.18.0) that allows to add support for backend without any change to Xarray

- [cfgrib](https://github.com/ecmwf/cfgrib) - GRIB
- [tiledb](https://github.com/TileDB-Inc/TileDB-CF-Py) - TileDB
- [rioxarray](https://corteva.github.io/rioxarray/stable/) - GeoTIFF, JPEG-2000, ESRI-hdr, etc (via GDAL)
- [xarray-sentinel](https://github.com/bopen/xarray-sentinel) - Sentinel-1 SAFE
- ...

## Why using the Xarray backend API

- Your users don't need to learn a new interface that is they can use `xr.open_dataset` with `engine` kwarg.
- With little extra effort you can have lazy loading with Dask. you have to implement a function for reading blocks and Xarray will manage lazy loading with Dask for you
- It's easy to implement: you don't need to integrate any code in Xarray

## Next

See the [documentation](https://docs.xarray.dev/en/stable/internals/how-to-add-new-backend.html) for more.

Follow the tutorial on creating a new backend for binary files.

```{tableofcontents}

```
