# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import time 


project = 'OPP'
copyright = f'{time.strftime("%Y")}, Природниче відділення, ВСП "Фаховий коледж ЧНУ"'
author = 'ЦК "Комп\'ютерні науки"'

master_doc = "index"
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions =["myst_parser", "sphinx_design", "sphinx.ext.autodoc"]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
language = 'uk_UA'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_logo = "_static/KN.jpg"
html_static_path = ['_static']
html_title = ""
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/nat-dep-clg-chnu-cs/opp",
    "repository_url": "https://github.com/nat-dep-clg-chnu-cs/opp",
    "repository_branch": "docs",
    "path_to_docs": "docs/source",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    #"announcment": "<b>v2.0.0</b> is now out! See the Changelog for details",
}
# -- MyST settings ---------------------------------------------------

myst_enable_extensions = ["deflist", "colon_fence"]
