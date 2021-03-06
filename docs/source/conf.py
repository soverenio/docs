# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config



# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os, sys
# sys.path.insert(0, os.path.abspath('.'))





# -- Project information -----------------------------------------------------

project = 'Soveren'
copyright = '2021, Soveren'
author = 'Soveren team'

# The full version, including alpha/beta/rc tags
release = '1.0'
version = 'latest'






# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#	'sphinxcontrib.golangdomain',
	'sphinx_inline_tabs',
	'sphinxcontrib.plantuml',
	'sphinx_copybutton',
    'sphinx_panels'
#   'hoverxref.extension'
#	'sphinxcontrib.contentui'
]

plantuml_output_format = 'svg'
plantuml_latex_output_format = 'png'

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

def setup(app):
    app.add_css_file('css/custom_furo.css')

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = []

# Sphinx uses html_extra_path option to add static files to the output (like
# robots.txt file).
# https://docs.readthedocs.io/en/stable/faq.html#how-can-i-avoid-search-results-having-a-deprecated-version-of-my-docs
html_extra_path = ['_public']







# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [ 'css/custom_furo.css' ]
#    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",

#html_logo = 'imgs/logo-soveren-dark.svg'

html_favicon = 'images/favicon1.png'

html_theme_options = {
# Customization options for Read the Docs theme
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'display_version': True,
#    'style_nav_header_background': '#FFFFFF',
#    'logo_only': True,
#    # Toc options
#    'collapse_navigation': False,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False

# Customization options for Furo theme
     "navigation_with_keys": True,
     "sidebar_hide_name": True,
     "light_logo": "Logo-dark-L.svg",
     "dark_logo": "Logo-dark-L.svg"
 }






# -- Options for LaTeX output -------------------------------------------------

#html_show_sphinx = False

#latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#    'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#    'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
 #   'preamble': r'''
 #       \usepackage{charter}
 #       \usepackage[defaultsans]{lato}
 #       \usepackage{inconsolata}
 #   ''',
#}

latex_logo = 'imgs/Logo_color@2x.png'