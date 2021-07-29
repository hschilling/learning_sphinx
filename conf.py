# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./src'))


# -- Project information -----------------------------------------------------

project = 'learn sphinx'
copyright = '2021, herb'
author = 'herb'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': 'https://mybinder.org', 'jupyterhub_url': '', 'thebe': False, 'colab_url': ''}, 'path_to_docs': '', 'repository_url': 'https://github.com/executablebooks/jupyter-book', 'repository_branch': 'master', 'google_analytics_id': '', 'extra_navbar': 'Powered by <a href="https://jupyterbook.org">Jupyter Book</a>', 'extra_footer': '', 'home_page_in_toc': True, 'use_repository_button': False, 'use_edit_page_button': False, 'use_issues_button': False}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
#html_static_path = ['om-theme/_static']

# if I put a file in that directory, it gets copied to 
# ./om-theme/_static/junk.html
# ./_build/html/_static/junk.html

# maybe because of this in the theme.conf file
#    html_static_path = ['om-theme/_static']



# my mods
# html_theme = 'sphinx_book_theme'
# html_css_files = ['custom.css']
# html_js_files = ['custom.js']


html_theme = 'om-theme' # use the theme in subdir 'theme'
html_theme_path = ['.'] # make sphinx search for themes in current dir


#html_extra_path=['om-theme/static/custom_search.html', 'om-theme/static/searchtools.js']
#html_extra_path=['om-theme/static/custom_search.html',]


#####  !!!!!!!!!!!!! if you put searchtools.js into the static folder, it goes into the _build/html/_static/searchtools.js and replaces the existing file

# html_extra_path=['index.html'] # if I put the index.html file in this same directory, it gets copied and used as the home page

# html_extra_path=['search.html'] # gets copied to ./_build/html/search.html and it is used for the search! But the styling is messed up

#   get a lot of errors like 
#           Loading failed for the <script> with source “file:///Users/hschilli/Documents/OpenMDAO/dev/learn-sphinx/_build/html/search_files/searchtools.js”

#           Loading failed for the <script> with source “file:///Users/hschilli/Documents/OpenMDAO/dev/learn-sphinx/_build/html/search_files/underscore.js”


# but the files are in

# ./_build/html/_static/searchtools.js
# ./_build/html/_static/search_files/searchtools.js
# ./_build/html/_static/js/searchtools.js


# this is really good
#      https://techwriter.documatt.com/sphinx-theming/themes.html

# the stuff from the inherited style goes in 

#  ./_build/html/_static

# including searchtools.js !


