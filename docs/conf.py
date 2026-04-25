import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Open MICKY'
copyright = '2026, FBOT@Research'
author = 'FBOT@Research'
release = '0.1'
language = 'pt_BR'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_options = {

    "light_logo": "team_images/logo_white.png",
    "dark_logo": "team_images/logo_black.png",

    "light_css_variables": {
        "color-brand-primary": "#ff5500", 
        "color-brand-content": "#ff5500", 
    },
    
    "dark_css_variables": {
        "color-brand-primary": "#ff5500", 
        "color-brand-content": "#ff5500", 
    },
    
    "sidebar_hide_name": True,

}

html_js_files = [
    "theme.js",
]

html_title = ""
html_theme = 'furo'
html_permalinks = False
html_static_path = ['_static']
html_css_files = ["css/custom.css"]
html_favicon = "_static/team_images/site_icon.ico"