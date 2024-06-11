# SciPy 2024

## Xarray: Friendly, Interactive, and Scalable Scientific Data Analysis

Organized by:

- Scott Henderson (Univ. Washington)
- Jessica Scheick (Univ. New Hampshire)
- Negin Sobhani (National Center for Atmospheric Research)
- Tom Nicholas [C]worthy
- Max Jones (CarbonPlan)
- Wietze Suijker (Space Intelligence)

## Learning Goals

- Learn how to leverage Xarray’s powerful backend and extension capabilities to customize workflows and open a variety of scientific datasets
- Effectively use Xarray’s multidimensional indexing operations
- Understand how Xarray can wrap other array types in the scientific Python ecosystem
- Understand how to apply custom functions to Xarray data structures
- Orient yourself to Xarray resources to continue on your Xarray journey!

## Outline

These are links to rendered webpages if you'd just like to read. Further down this page is an 'Instructions' section that explains how to spin up an interactive computing environment.

```{dropdown} Introduction
{doc}`../../overview/get-started`

{doc}`../../fundamentals/02.1_indexing_Basic`

TODO: Domain-agnositic data model, backends/engines
```

```{dropdown} Indexing and Computation
{doc}`../../intermediate/indexing/advanced-indexing`

{doc}`../../intermediate/01-high-level-computation-patterns`

{doc}`../../intermediate/xarray_and_dask`
```

```{dropdown} Extending & Customizing Xarray
{doc}`../../advanced/01_accessor_examples.ipynb`

{doc}`../../advanced/1.Backend_without_Lazy_Loading.ipynb
```

```{dropdown} Synthesis
TODO: A Guided 'bring-your-own data exercise
```

## Instructions

### Running Locally

See instructions to set up the environment for running the tutorial material [here](get-started).

### Github Codespaces

This tutorial is available to run within [Github Codespaces](https://github.com/features/codespaces) - "a development environment that's hosted in the cloud" - with the conda environment specification in the [`conda-lock.yml`](../../conda/conda-lock.yml) file.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/xarray-contrib/xarray-tutorial/tree/main?devcontainer_path=.devcontainer%2Fscipy2023%2Fdevcontainer.json)

☝️ Click the button above to go to options window to launch a Github codespace.

A codespace is a development environment that's hosted in the cloud.
You can choose from a selection of virtual machine types: 2 cores - 4 GB RAM - 32 GB storage, and 4 cores - 8 GB RAM - 32GB storage.
Additionally, you are able to chose from various Dev container configuration, for this specific workshop, please ensure that `Scipy2024` is selected.
GitHub currently gives every user [120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts), beyond that you must pay. **So be sure to explicitly stop or shut down your codespace when you are done by going to this page (https://github.com/codespaces).**

Once your codespace is launched, the following happens:

- [Visual Studio Code](https://code.visualstudio.com/) Interface will open up within your browser.
- A built in terminal will open and it will execute `jupyter lab` automatically.
- Once you see a url to click within the terminal, simply `cmd + click` the given url.
- This will open up another tab in your browser, leading to a [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/) Interface.
