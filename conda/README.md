# Install unpinned environment:

```
mamba env create -f environment-unpinned.yml
mamba activate xarray-tutorial
```

## Install locked environment:

https://github.com/conda-incubator/conda-lock

```
conda-lock install
```

\*Or on Linux: `mamba env create -f .binder/environment.yml`

## Create/update multiplatform lockfile:

```
conda-lock lock --mamba -f environment-unpinned.yml -p osx-64 -p linux-64 -p win-64
```

## Render a mybinder.org compatible locked file

```
conda-lock render -k env
mv conda-linux-64.lock.yml environment.yml
```
