# Xarray Tutorial

[![CI](https://github.com/xarray-contrib/xarray-tutorial/workflows/CI/badge.svg?branch=main)](https://github.com/xarray-contrib/xarray-tutorial/actions?query=branch%3Amain)
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://tutorial.xarray.dev)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/HEAD?labpath=index.ipynb)

This is the repository for a Jupyter Book website with tutorial material for [Xarray](https://github.com/pydata/xarray), _an open source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun!_

The website is hosted at https://tutorial.xarray.dev

Tutorials are written as interactive Jupyter Notebooks with executable code examples that you can easily run and modify:

#### On the Cloud

All notebooks can be run via the Mybinder.org 'Launch Binder' badge at the top of this page. This will load a pre-configured JupyterLab interface with all tutorial notebooks for you to run. _You have minimal computing resources and any changes you make will not be saved._

#### Locally

You can also run these notebooks on your own computer! We recommend using [`conda-lock`](https://conda-incubator.github.io/conda-lock/) to ensure a fully reproducible Python environment:

```bash
git clone https://github.com/xarray-contrib/xarray-tutorial.git
cd xarray-tutorial

conda-lock install conda/conda-lock.yml --name xarray-tutorial
# Or latest package versions: `mamba env create -f conda/environment-unpinned.yml`

conda activate xarray-tutorial
jupyter lab
```

## Contributing

Contributions are welcome and greatly appreciated! See our [CONTRIBUTING.md](./CONTRIBUTING.md) document.
