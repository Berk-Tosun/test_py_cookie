import os
import sys

import test_py_cookie

sys.path.insert(0, os.path.abspath(".."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "test-py-cookie"
copyright = "2023, Berk Tosun"
author = "Berk Tosun"
release = test_py_cookie.__version__
version = test_py_cookie.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    # "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxcontrib.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx_autodoc_typehints",
    # "sphinx_copybutton",
    # "sphinx.ext.todo",
    # "sphinxcontrib.mermaid",
]
autosummary_generate = True
autodoc_member_order = "bysource"
napoleon_google_docstring = True
# autosectionlabel_prefix_document = True
# todo_include_todos = True
myst_heading_anchors = 6  # create anchors for h1-h6
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "html_admonition",
]

source_suffix = {
    ".rst": "restructuredtext",
    # ".ipynb": "myst-nb",
    # ".myst": "myst-nb",
}

templates_path = ["_templates"]
exclude_patterns = []  # type: ignore


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
