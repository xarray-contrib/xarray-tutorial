<img src="https://docs.xarray.dev/en/stable/_static/dataset-diagram-logo.png" align="right" width="30%">

(get-started)=

# Get Started

Most of the tutorial content here is written as Jupyter Notebooks that mix
code, text, visualization, and exercises. You can either browse rendered versions of these notebooks on this website, or _execute_ the code examples interactively.

You have two options for executing notebooks:

**1. On the Cloud:** Clicking [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/HEAD?labpath=overview/fundamental-path/index.ipynb) will load a pre-configured Jupyter Lab interface with _all_ tutorial notebooks for you to run. _You have minimal computing resources and any changes you make will not be saved._ Any page with executable content also has a {octicon}`rocket;2em` icon in the upper right that will launch an interactive session for that particular page.

```{warning}
Be patient, it can take a few minutes for a server to become available on the Cloud (Mybinder.org)!
```

**1. On your computer:** Running tutorials on your computer requires some setup:

We recommend using [`conda-lock`](https://conda.github.io/conda-lock/) to ensure a fully reproducible Python environment

```
git clone https://github.com/xarray-contrib/xarray-tutorial.git
cd xarray-tutorial

conda-lock install conda/conda-lock.yml --name xarray-tutorial
# Or latest package versions: `mamba env create -f conda/environment-unpinned.yml`

conda activate xarray-tutorial
jupyter lab
```

## Organization

Tutorials are approximately divided into sections with increasing levels of complexity: `Fundamentals`, `Intermediate`, `Advanced`. You'll also find content specific to various `Workshops` hosted over the years, often with accompanying video recordings of instructors going over content and answering questions that come up.

## Jupyter Lab

JupyterLab is a next-generation web-based user interface for Project Jupyter. If you are new to this interface, spend some time reviewing the [documentation and videos](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html).

## Jupyter Notebooks

If you haven't used the Jupyter Notebooks before, the quick intro is

1. There are two modes: command and edit
1. From command mode, press Enter to edit a cell (like this markdown cell)
1. From edit mode, press Esc to change to command mode
1. Press shift+enter to execute a cell and move to the next cell.
1. The toolbar has commands for executing, converting, and creating cells.
