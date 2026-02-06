# Xarray Tutorial

[![Deploy Website to GitHub Pages](https://github.com/xarray-contrib/xarray-tutorial/actions/workflows/main.yaml/badge.svg)](https://github.com/xarray-contrib/xarray-tutorial/actions/workflows/main.yaml)
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://tutorial.xarray.dev)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/HEAD?labpath=workshops/scipy2025/index.ipynb)

This is the repository for a Jupyter Book website with tutorial material for [Xarray](https://github.com/pydata/xarray), _an open source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun!_

The website is hosted at https://tutorial.xarray.dev

Tutorials are written as interactive Jupyter Notebooks with executable code examples that you can easily run and modify:

#### On the Cloud

All notebooks can be run via the Mybinder.org 'Launch Binder' badge at the top of this page. This will load a pre-configured JupyterLab interface with all tutorial notebooks for you to run. _You have minimal computing resources and any changes you make will not be saved._

#### Github Codespaces

This tutorial is available to run within [Github Codespaces](https://github.com/features/codespaces) - "a development environment that's hosted in the cloud"

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/xarray-contrib/xarray-tutorial/tree/main)

☝️ Click the button above to go to options window to launch a Github codespace.

GitHub currently gives every user [120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts), beyond that you must pay. **So be sure to explicitly stop or shut down your codespace when you are done by going to this page (https://github.com/codespaces).**

You can also use the GitHub CLI to launch a codespace

```
# This will output a URL to use VSCode in the browser
gh codespace create --repo xarray-contrib/xarray-tutorial
# Optionally launch JupyterLab instead of vscode (after codespace has been created)
gh codespace jupyter
```

#### Locally

You can also run these notebooks on your own computer! We recommend using [`pixi`](https://pixi.sh/latest/#installation) to ensure a fully reproducible Python environment:

```bash
git clone https://github.com/xarray-contrib/xarray-tutorial.git
cd xarray-tutorial
pixi run tutorial
```

### Building the Documentation Locally

To build and serve the tutorial website locally with live reload:

```bash
pixi run watch
```

This watches for changes, rebuilds, and serves at http://localhost:8000.

To build without serving:

```bash
pixi run build
```

## Contributing

Contributions are welcome and greatly appreciated! See our [CONTRIBUTING.md](./CONTRIBUTING.md) document.

Thanks to our contributors so far!

[![Contributors](https://contrib.rocks/image?repo=xarray-contrib/xarray-tutorial)](https://github.com/xarray-contrib/xarray-tutorial/graphs/contributors)

## Acknowledgements

This website is the result of many contributions from the Xarray community! We're very grateful for everyone's volunteered effort as well as [sponsored development](https://xarray.dev/#sponsors). Funding for SciPy 2022, SciPy 2023 tutorial material development specifically was supported by NASA's Open Source Tools, Frameworks, and Libraries Program (award 80NSSC22K0345).
