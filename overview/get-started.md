<img src="https://docs.xarray.dev/en/stable/_static/Xarray_Logo_RGB_Final.svg" align="right" width="30%">

(get-started)=

# Get Started

## Organization

Tutorials are approximately divided into sections with increasing levels of complexity: `Fundamentals`, `Intermediate`, `Advanced`. You'll also find content specific to various `Workshops` hosted over the years, often with accompanying video recordings of instructors going over content and answering questions that come up.

Most of the tutorial content is written as Jupyter Notebooks that mix
code, text, visualization, and exercises. You can either browse rendered versions of these notebooks on this website, or _execute_ the code examples interactively.

Many notebooks use special formatting ([Myst Markdown](https://mystmd.org/guide/quickstart-jupyter-lab-myst)) that renders best in a JupyterLab web interface. If you are new to JupyterLab, spend some time reviewing the [documentation and videos](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html).

## Run code interactively

### On the Cloud

The easiest way to start modifying and experimenting with tutorial content is to launch a pre-configured server on the Cloud. This is easy thanks to several free resources which offer ephemeral computing instances (be aware you may loose your connection or work at any time)

#### Mybinder.org

Clicking [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/HEAD) will load a pre-configured Jupyter Lab interface with _all_ tutorial notebooks for you to run. _You have minimal computing resources and any changes you make will not be saved._ Any page with executable content also has a {octicon}`rocket;2em` icon in the upper right that will launch an interactive session for that particular page.

```{warning}
Be patient, it can take a few minutes for a server to become available on the Cloud (Mybinder.org)!
```

#### GitHub Codespaces

This tutorial is available to run within [GitHub Codespaces](https://github.com/features/codespaces) - a preconfigured development environment running in Microsoft Azure.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/xarray-contrib/xarray-tutorial)

☝️ Click the button above to go to options window to launch a GitHub codespace.

You can choose from a selection of virtual machine types: 2 cores - 8 GB RAM should be sufficient for all code examples in this repository.
Additionally, you are able to chose from various configurations for specific workshops (such as Scipy2024).
GitHub currently gives every user [120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts), beyond that you must pay. **So be sure to explicitly stop your codespace when you are done by going to this page (https://github.com/codespaces).** You can also chose to fully delete your codespace when you're done exploring tutorial content.

### On your computer

Running tutorials on your computer requires some setup:

We recommend using [`conda-lock`](https://conda.github.io/conda-lock/) to ensure a fully reproducible Python environment

```
git clone https://github.com/xarray-contrib/xarray-tutorial.git
cd xarray-tutorial

conda-lock install conda/conda-lock.yml --name xarray-tutorial
# Or latest package versions: `mamba env create -f conda/environment-unpinned.yml`

conda activate xarray-tutorial
jupyter lab
```
