# Contributing Guide

This tutorial repository is a great opportunity to start contributing to Xarray.

- Report bugs, request features or submit feedback as a [GitHub Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues). First check existing [issues](https://github.com/xarray-contrib/xarray-tutorial/issues) !

- Make fixes, add content or improvements using [GitHub Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), the sections below go over this process in more detail:

```{seealso}
The Project Pythia Foundations material on  [Github](https://foundations.projectpythia.org/foundations/getting-started-github.html) and Github workflows is a great place to start if you are new to this.
```

## Content Guidelines

Please note that examples submitted to this repository should follow these
guidelines:

1. Run top-to-bottom without intervention from the user
1. Not require external data sources that may disappear over time (external data sources that are highly unlikely to disappear are fine). Small datasets for tutorial purposes can be added [here](https://github.com/pydata/xarray-data/) if necessary.
1. Not be resource intensive, and should run within 2GB of memory
1. Be clear and contain enough prose to explain the topic at hand
1. Be concise and limited to one or two topics, such that a reader can get through the example within a few minutes of reading
1. Be of general relevance to Xarray users, and so not too specific on a particular problem or use case.

## Contribution process

### Fork this repository

We recommend first forking this repository and creating a local copy:

```
git clone https://github.com/YOURACCOUNT/xarray-tutorial.git
cd xarray-tutorial
```

### Create a Python environment

You'll need `pixi` or `conda` or `mamba`, which can be installed from https://github.com/conda-forge/miniforge

We also use [pre-commit hooks](https://pre-commit.com) to run styling and other checks before committing code.

#### Using pixi (recommended)

```
pixi install
pixi shell  # exit
```

#### Using conda

```
mamba env create -f .binder/environment.yml -n xarray-tutorial
conda activate xarray-tutorial  # conda deactivate
pre-commit install
```

### Add content

Develop your new content on a branch. See [JupyterBook Docs](https://jupyterbook.org/en/stable/intro.html) for guides on adding `.md`, `.ipynb` and other content.

```
git checkout -b newcontent
git add .
git commit -m "added pages x,y and improved z"
```

### Preview your changes

Running jupyterbook will execute notebooks and render HTML pages for the website. Be sure to fix any execution errors and preview the website in your web browser to make sure everything looks good!

```
jupyter-book build ./ --warningiserror --keep-going
# Or "pixi run build"
```

### Open a pull request

```
git push
```

Follow the link reported in a terminal to open a pull request!

## Instructions for environment management

[`pixi`](https://pixi.sh) can be used to create and update a multi-platform lockfile, so a reproducible set of package versions is installed across different operating systems.

Dependencies (with optional pins) are specified in the `pyproject.toml` file, and specific locked versions for all platforms are kept in `pixi.lock`.

Install environment from the lockfile

```
pixi install
pixi shell # activate environment, "exit" to deactivate
```

Upgrade all packages to latest versions:

```
pixi upgrade
```

## Render conda/mamba environment files

```
pixi project export conda-environment -p linux-64 .binder/environment.yml
pixi project export conda-explicit-spec -p linux-64 /tmp
```
