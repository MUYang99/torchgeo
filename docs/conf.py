# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

import pytorch_sphinx_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

import torchgeo

# -- Project information -----------------------------------------------------

project = 'torchgeo'
copyright = '2021, Microsoft Corporation'
author = torchgeo.__author__
version = '.'.join(torchgeo.__version__.split('.')[:2])
release = torchgeo.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'nbsphinx',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# Sphinx 4.0+ required for autodoc_typehints_description_traget
needs_sphinx = '4.0'

nitpicky = True
nitpick_ignore = [
    # Undocumented classes
    ('py:class', 'fiona.model.Feature'),
    ('py:class', 'kornia.augmentation._2d.intensity.base.IntensityAugmentationBase2D'),
    ('py:class', 'kornia.augmentation._3d.geometric.base.GeometricAugmentationBase3D'),
    ('py:class', 'kornia.augmentation.base._AugmentationBase'),
    ('py:class', 'lightning.pytorch.utilities.types.LRSchedulerConfig'),
    ('py:class', 'lightning.pytorch.utilities.types.OptimizerConfig'),
    ('py:class', 'lightning.pytorch.utilities.types.OptimizerLRSchedulerConfig'),
    ('py:class', 'segmentation_models_pytorch.base.model.SegmentationModel'),
    ('py:class', 'timm.models.resnet.ResNet'),
    ('py:class', 'timm.models.vision_transformer.VisionTransformer'),
    ('py:class', 'torch.optim.lr_scheduler.LRScheduler'),
    ('py:class', 'torchvision.models._api.WeightsEnum'),
    ('py:class', 'torchvision.models.resnet.ResNet'),
    ('py:class', 'torchvision.models.swin_transformer.SwinTransformer'),
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
    'pytorch_project': 'docs',
    'navigation_with_keys': True,
    'analytics_id': 'UA-209075005-1',
}

html_favicon = os.path.join('..', 'logo', 'favicon.ico')

html_static_path = ['_static']
html_css_files = ['badge-height.css', 'notebook-prompt.css', 'table-scroll.css']

# -- Extension configuration -------------------------------------------------

# sphinx.ext.autodoc
autodoc_default_options = {
    'members': True,
    'special-members': True,
    'show-inheritance': True,
}
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'

# sphinx.ext.intersphinx
intersphinx_mapping = {
    'einops': ('https://einops.rocks/', None),
    'kornia': ('https://kornia.readthedocs.io/en/stable/', None),
    'lightning': ('https://lightning.ai/docs/pytorch/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'pyproj': ('https://pyproj4.github.io/pyproj/stable/', None),
    'python': ('https://docs.python.org/3', None),
    'rasterio': ('https://rasterio.readthedocs.io/en/stable/', None),
    'segmentation_models_pytorch': ('https://smp.readthedocs.io/en/stable/', None),
    'shapely': ('https://shapely.readthedocs.io/en/stable/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'timm': ('https://huggingface.co/docs/timm/main/en/', None),
    'torch': ('https://docs.pytorch.org/docs/stable/', None),
    'torchmetrics': ('https://lightning.ai/docs/torchmetrics/stable/', None),
    'torchvision': ('https://docs.pytorch.org/vision/stable/', None),
    'ultralytics': ('https://docs.ultralytics.com/', None),
}

# nbsphinx
nbsphinx_execute = 'never'
with open(os.path.join('tutorials', 'prolog.rst.jinja')) as f:
    nbsphinx_prolog = f.read()

# Disables requirejs in nbsphinx to enable compatibility with the pytorch_sphinx_theme
# See more information here https://github.com/spatialaudio/nbsphinx/issues/599
# NOTE: This will likely break nbsphinx widgets
nbsphinx_requirejs_path = ''
