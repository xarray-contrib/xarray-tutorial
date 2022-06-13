# Xarray Tutorial

[![CI](https://github.com/xarray-contrib/xarray-tutorial/workflows/CI/badge.svg?branch=main)](https://github.com/xarray-contrib/xarray-tutorial/actions?query=branch%3Amain)
[![Jupyter Book Badge](docs/images/badge.svg)](https://tutorial.xarray.dev)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/HEAD?urlpath=lab)

This is the repository for a JupyterBook website with tutorial material for [Xarray](https://github.com/pydata/xarray), an open source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun.

You can browse the website at https://tutorial.xarray.dev

## Running code examples

Much of the tutorial is written as Jupyter Notebooks with executable code examples

#### On the Cloud

The easiest way to run these examples is via a [mybinder.org](https://mybinder.org), by clicking the badge at the top of this page. This will load a pre-configured JupyterLab interface with all tutorial notebooks for you to run. _You have minimal computing resources and any changes you make will not be saved._

#### Locally

You can also run these notebooks on your own computer! We recommend using [`conda-lock`](https://conda-incubator.github.io/conda-lock/) to ensure a fully reproducible Python environment:

```bash
git clone https://github.com/xarray-contrib/xarray-tutorial.git
cd xarray-tutorial

conda-lock install -f conda/conda-lock.yml --name xarray-tutorial
# Or latest package versions: `mamba env create -f conda/environment-unpinned.yml`

conda activate xarray-tutorial
jupyter lab
```

## Contributing

Contributions are welcome and greatly appreciated! See our [CONTRIBUTING.md](./CONTRIBUTING.md) document.
