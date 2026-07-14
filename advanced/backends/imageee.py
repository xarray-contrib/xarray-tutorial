# %% [markdown]
# # Create your own Xarray Backend
# In this lesson, we will learn about and how to create your own custom xarray backend
#
# :::{admonition} Learning Goals
# - Learn about xarray's support for custom backends
# - Learn how to use a custom `imageio` backend to open and manipulate GIFs
# - Learn how to extend the `imagegio` backend to write out a GIF
# :::
#
# ## Why should you create your own Xarray backend?
#
# - Allows you to use xarray's interface
#     - Attribute-like syntax, dict-like syntax and label based indexing
# - You don’t need to integrate any code in Xarray
# - Easy and fast!
#

# %% [markdown]
# ## Setting up the BackendEntrypoint
#
# To set up a `BackendEntrypoint` we can implement a subclass of `BackendEntrypoint` and expose the `open_dataset` method to it. For this tutorial we have the `ImageIOBackend` already defined but we will extend the functionally to write GIFS.

# %%
image_path = "io.gif"

# %% [markdown]
# We can write a simple image reader function that we can then plug into our `MyBackendEntrypoint` class. For this example we are going to use `imageio` an image reader and writer library. With `imageio` you can read an image file with `iio.imopen`
#
# :::{note}
# The `ImageIOBackend` also defines a `ImageIOBackendArray` with basic indexing.
# :

# %%
import imageio as iio
from xarray.backends import BackendEntrypoint


def imageio_open(
    filename_or_obj,
):
    img = iio.imopen(filename_or_obj, io_mode="r")
    return img.read()


class MyImageReader(BackendEntrypoint):
    def open_dataset(
        self,
        filename_or_obj,
        *,
        drop_variables=None,
    ):
        return imageio_open(filename_or_obj)


type(MyImageReader().open_dataset(image_path))

# %% [markdown]
# ## Reading image data
#
# Lets use our `ImageIOBackend` to open a GIF.
#

# %%
import xarray as xr
from imageio_ import ImageIOBackend

gif_ds = xr.open_dataset(image_path, engine=ImageIOBackend)

# %% [markdown]
# ### Examining our image dataset
#
# Since our image is a `Dataset` object we can use xarray's interface for `Dataset` objects.
#
# Let's try listing all of the variables, dimensions and selecting data

# %%

# %% [markdown]
# We can list our dimensions

# %%

# %% [markdown]
# Let's try getting our `DataArray`

# %%

# %% [markdown]
# ## GIF metadata
# We can examine, update and add metadata to our `Dataset` object.
#
# We can examine the attributes in our GIF "data" variable with the `.attrs` method

# %%

# %% [markdown]
# ## Exercise

# %% [markdown]
# ::::{admonition} Exercise
# :class: tip
#
# Can you add a new attribute to our GIF "data" variable called "fps". This is the frames per second we can write our GIF to. You can set it to any value.
#
# :::{admonition} Solution
# :class: dropdown
#
# ```python
# gif_ds.data.attrs['fps'] = 100
# ```
# :::
# ::::

# %% [markdown]
# ### GIF writer
# We can extend our backend with an GIF writer. Here we use `matplotlib`'s animation functions and `PillowWriter`

# %%
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from imageio_ import ImageIOBackend
from matplotlib.animation import PillowWriter


class SimpleImageWriter(ImageIOBackend):
    def to_giff(
        self,
        dataset,
        variable,
        time_dim,
        out_filename,
        **kwargs,
    ):
        fig, ax = plt.subplots()

        frames = []
        variable_da = dataset[variable]
        X, Y = np.meshgrid(variable_da.height, variable_da.width)
        for time in variable_da[time_dim]:
            variable_da = variable_da.transpose("time", "width", "height", "color")
            to_plot = ax.pcolormesh(
                X,
                Y,
                variable_da.sel(time=time).isel(color=0),
                # animated=True,
                shading="auto",
                **kwargs,
            )

            frames.append([to_plot])

        try:
            writer = PillowWriter(fps=variable_da.attrs["fps"], **kwargs)
        except KeyError:
            writer = PillowWriter(fps=50, **kwargs)

        ani = animation.ArtistAnimation(fig, frames, blit=True, repeat=True)
        ani.save(filename=out_filename, writer=writer)


# %%
img_writer = SimpleImageWriter()
img_writer.to_giff(gif_ds, "data", "time", "io_writer.gif")

# %%
