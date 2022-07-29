# Parallelizing custom functions

Almost all of xarray’s built-in operations work on Dask arrays.

Sometimes analysis calls for functions that aren't in xarray's API (e.g. scipy).
There are three ways to apply these functions in parallel on each block of your
xarray object:

1. Extract Dask arrays from xarray objects ([.data](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.data.html)) and use Dask directly e.g.
   ([apply_gufunc](https://docs.dask.org/en/latest/generated/dask.array.gufunc.apply_gufunc.html), [map_blocks](https://docs.dask.org/en/latest/generated/dask.array.map_blocks.html), [map_overlap](https://docs.dask.org/en/latest/generated/dask.array.map_overlap.html), [blockwise](https://docs.dask.org/en/latest/generated/dask.array.core.blockwise.html), [reduction](https://docs.dask.org/en/latest/generated/dask.array.reduction.html)). Then wrap the result as an Xarray object.

2. Use [apply_ufunc](https://docs.xarray.dev/en/stable/generated/xarray.apply_ufunc.html) to apply functions that consume and return duck arrays. This automates extracting the data from Xarray objects, applying a function, and then converting the bare array result back to a Xarray object.

3. Use [map_blocks](https://docs.xarray.dev/en/stable/generated/xarray.map_blocks.html), [Dataset.map_blocks](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.map_blocks.html) or [DataArray.map_blocks](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.map_blocks.html)
   to apply functions that consume and return xarray objects.

Which method you use ultimately depends on the type of input objects expected by
the function you're wrapping, and the level of performance or convenience you
desire.
