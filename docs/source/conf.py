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

extensions =["myst_parser", 
             "sphinx_design", 
             "sphinx.ext.autodoc",
             "sphinxcontrib.mermaid",
             "sphinx.ext.imgconverter",
             'matplotlib.sphinxext.plot_directive',
             'sphinxcontrib.tikz',
             ]
    
tikz_proc_suite = 'GhostScript'
tikz_includegraphics_path = '_static/'
tikz_latex_preamble = r'''\usepackage[utf8]{inputenc}
\usepackage[utf8]{inputenc}
        \usepackage[T2A,T1]{fontenc}
\usepackage[ukrainian]{babel}
\usepackage{datatool}
\usepackage{graphicx}
\usepackage{pgfplotstable}
'''
templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
language = 'uk_UA'
locale_dirs = ['_locale/']
source_encoding = 'utf-8'
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/KN.jpg"
html_static_path = ['_static']
html_title = ""
html_theme_options = {
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/PyData",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/pydata/pydata-sphinx-theme",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Домашня",
            "url": "https://nat-dep-clg-chnu-cs.github.io/opp/",
            "icon": "fa fa-home",
        },

    ],
    "use_edit_page_button": True,
    "navbar_align": "left", 
    #"announcment": "<b>v2.0.0</b> is now out! See the Changelog for details",
}

html_context = {
    "github_user": "nat-dep-clg-chnu-cs",
    "github_repo": "opp",
    "github_version": "docs",
    "doc_path": "docs/source",
}

# -- MyST settings ---------------------------------------------------

myst_enable_extensions = ["deflist", "colon_fence", "attrs_block", "attrs_inline","fieldlist"]
myst_url_schemes = {
        "standart": "https://mon.gov.ua/storage/app/media/Fakhova%20peredvyshcha%20osvita/Zatverdzheni.standarty/2021/11/30/122-Kompyuterni.nauky.30.11.pdf"
        }
myst_heading_anchors = 2
TITLE = open('title.tex', 'r').read()
latex_engine = 'pdflatex'
latex_theme = 'howto'
latex_elements = {
    'papersize': 'a4paper',
    'inputenc': '\\usepackage[utf8]{inputenc} ',
#    'fontenc': '\\usepackage[T2A,T1]{fontenc}',
#    'fontpkg': r'''
#\setmainfont{DejaVu Serif}
#\setsansfont{DejaVu Sans}
#\setmonofont{DejaVu Sans Mono}
#''', 
    'pointsize': '12pt',
    'preamble': r'\usepackage{mystyle}',    
    'babel': r'''\usepackage[ukrainian]{babel}''',
    'geometry': r'''\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}''',
    'maketitle': TITLE,
}
latex_logo = '_static/KN.jpg'
latex_show_urls = 'footnote'
latex_additional_files = ["mystyle.sty"]
