# SciPy 2023

## Xarray: Friendly, Interactive, and Scalable Scientific Data Analysis

Organized by:

- Deepak Cherian (National Center for Atmospheric Research)
- Scott Henderson (Univ. Washington)
- Jessica Scheick (Univ. New Hampshire)
- Negin Sobhani (National Center for Atmospheric Research)
- Tom Nicholas (Lamont-Doherty Earth Observatory)
- Anderson Banihirwe (CarbonPlan)
- Don Setiawan (Univ. Washington)

## Instructions

### Nebari

For the live tutorial, we will be using the SciPy 2023 Nebari JupyterHub at [scipy.quansight.dev](https://scipy.quansight.dev/)

You can follow [this participants' guide to register and sign-in to Nebari](https://docs.google.com/document/d/1vnWhNyUBRpILb2MAHQfTmZQY3pCIaCmroV9ke49nQlE/edit), and:

- Use this link to clone the tutorial materials:

```
https://github.com/xarray-contrib/xarray-tutorial.git
```

- Select `global-global-xarray` environment for the notebooks when prompted.

### Running Locally

See instructions to set up the environment for running the tutorial material [here](get-started).

### Github Codespaces

This tutorial is available to run within [Github Codespaces](https://github.com/features/codespaces) - "a development environment that's hosted in the cloud" - with the conda environment specification in the [`conda-lock.yml`](../../conda/conda-lock.yml) file.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/xarray-contrib/xarray-tutorial/tree/main?devcontainer_path=.devcontainer%2Fscipy2023%2Fdevcontainer.json)

☝️ Click the button above to go to options window to launch a Github codespace.

A codespace is a development environment that's hosted in the cloud.
You can choose from a selection of virtual machine types: 2 cores - 4 GB RAM - 32 GB storage, and 4 cores - 8 GB RAM - 32GB storage.
Additionally, you are able to chose from various Dev container configuration, for this specific workshop, please ensure that `Scipy2023` is selected.
GitHub currently gives every user [120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts), beyond that you must pay. **So be sure to explicitly stop or shut down your codespace when you are done by going to this page (https://github.com/codespaces).**

Once your codespace is launched, the following happens:

- [Visual Studio Code](https://code.visualstudio.com/) Interface will open up within your browser.
- A built in terminal will open and it will execute `jupyter lab` automatically.
- Once you see a url to click within the terminal, simply `cmd + click` the given url.
- This will open up another tab in your browser, leading to a [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/) Interface.

## Outline

```{dropdown} Introduction
{doc}`../../overview/get-started`
```

```{dropdown} Indexing

```

```{dropdown} Computational Patterns
{doc}`../../intermediate/01-high-level-computation-patterns`
```

```{dropdown} Wrapping other arrays: dask
{doc}`../../intermediate/xarray_and_dask`
```

```{dropdown} Wrapping custom computation
{doc}`../../advanced/apply_ufunc/simple_numpy_apply_ufunc`

{doc}`../../advanced/apply_ufunc/core-dimensions`

{doc}`../../advanced/apply_ufunc/complex-output-numpy`

{doc}`Explore the remaining material <../../advanced/apply_ufunc/apply_ufunc>`
```
