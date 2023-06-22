# Instructions for environment management

## Install locked environment:

`conda-lock` can be used to create a multi-platform lockfile, so a reproducible set of package versions is installed across different operating systems. https://conda-incubator.github.io/conda-lock/

```
conda-lock install
```

\*Or on Linux: `mamba env create -f .binder/environment.yml`

## Create/update multiplatform lockfile:

```
conda-lock lock --mamba -f environment-unpinned.yml -p osx-64 -p linux-64 -p win-64 -p osx-arm64
```

## Render a mybinder.org compatible environment.yml (linux-64)

```
conda-lock render -k env -p linux-64
mv conda-linux-64.lock.yml environment.yml
```

## Install unpinned environment:

If you want to run tutorials with the latest versions of compatible packages

If you need to install mamba see https://github.com/conda-forge/miniforge#mambaforge

```
mamba env create -f environment-unpinned.yml
mamba activate xarray-tutorial
```
