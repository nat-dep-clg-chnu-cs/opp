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
             "sphinxcontrib.mermaid"
             ]
    
mermaid_params = ['-p' 'puppeteer-config.json']


templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
language = 'uk_UA'
locale_dirs = ['_locale']
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

myst_enable_extensions = ["deflist", "colon_fence", "attrs_block", "attrs_inline"]
myst_heading_anchors = 2

latex_engine = 'pdflatex'
latex_theme = 'howto'
latex_elements = {
    'papersize': 'a4paper',
    'inputenc': '\\usepackage[utf8]{inputenc}',
           'pointsize': '12pt',
    'preamble': r'''
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
%\usepackage{setspace}
%\usepackage{xcolor}
\usepackage{array}
\usepackage{multirow}
\usepackage{lscape}
\usepackage{pdflscape}
\usepackage{everypage}
%\usepackage[printwatermark]{xwatermark}
\renewcommand{\baselinestretch}{1.0}

\newcommand{\tabcomp}[1]{\rotatebox[origin=c]{90}{\parbox[c]{2cm}{\centering #1 }}}
\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}

\newcommand{\galuz}{12 <<Інформаційні технології>>}
\newcommand{\spec}{122 <<Комп'ютерні науки>>}

\newcommand{\Lpagenumber}{\ifdim\textwidth=\linewidth\else\bgroup
  \dimendef\margin=0 %use \margin instead of \dimen0
  \ifodd\value{page}\margin=\oddsidemargin
  \else\margin=\evensidemargin
  \fi
  \raisebox{\dimexpr -\topmargin-\headheight-\headsep-0.5\linewidth}[0pt][0pt]{%
    \rlap{\hspace{\dimexpr \margin+\textheight+\footskip}%
    \llap{\rotatebox{90}{\thepage}}}}%
\egroup\fi}
\AddEverypageHook{\Lpagenumber}%
    ''',
    'babel': r'''
    \usepackage[ukrainian]{babel}
    ''',
    
    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1
        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge {ОСВІТНЬО-ПРОФЕСІЙНА ПРОГРАМА}}

            \vspace{0mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=1.3]{KN.jpg}
            \end{figure}

            \vspace{0mm}
            \Large \textbf{{<<КОМП'ЮТЕРНІ НАУКИ>>}}


            \vspace*{0mm}


            %% \vfill adds at the bottom
            \vfill
            \small \textit{Більше корисної інформації можна дізнатися на }{\href{http://college.chnu.edu.ua/}{ВСП <<Фаховий коледж ЧНУ>>}}
        \end{titlepage}


        \begin{titlepage}
            \begin{center}

\begin{normalsize}
\textbf{МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ\\
Чернівецький національний університет імені Юрія Федьковича\\}
\end{normalsize}
{\small  \textbf{Відокремлений структурний підрозділ "Фаховий коледж Чернівецького національного університету імені Юрія Федьковича"}}

\end{center}\vspace{1cm}

\begin{flushright}
\begin{minipage}{9.5cm}
\hyphenpenalty=10000
<<ЗАТВЕРДЖЕНО>>\\
Вченою радою Чернівецького національного університету імені Юрія Федьковича
Голова Вченої ради, ректор
\underline{\hspace{2.7cm}}~Р.І.~Петришин\\
%<<\underline{\hspace{1cm}}>> \underline{\hspace{3cm}} 2018 р.\\
Протокол №\underline{\hspace{0.7cm}} від <<\underline{\hspace{0.7cm}}>> \underline{\hspace{2cm}}  20\underline{\hspace{0.7cm}}~р.\\
\end{minipage}
\end{flushright}

\begin{center}
\textbf{ОСВІТНЬО-ПРОФЕСІЙНА ПРОГРАМА\\
<<КОМП'ЮТЕРНІ НАУКИ>>\\
фахової передвищої освіти
}
\end{center}
\begin{center}
\begin{tabular}{ L{5cm}  C{10cm}}

  ГАЛУЗЬ ЗНАНЬ & \textbf{\galuz}\\
\cline{2-2}
СПЕЦІАЛЬНІСТЬ & \textbf{\spec}\\
\cline{2-2}
КВАЛІФІКАЦІЯ & \textbf{фаховий молодший бакалавр з комп’ютерних наук} \\




\cline{2-2}

\end{tabular}
\end{center}



\begin{flushright}
\begin{minipage}{9.5cm}
СХВАЛЕНО

на засіданні Педагогічної ради\\ ВСП <<Фаховий коледж ЧНУ>>\\
Протокол №\underline{\hspace{0.7cm}} від <<\underline{\hspace{0.7cm}}>> \underline{\hspace{2cm}}  20\underline{\hspace{0.7cm}}~р.\\

Голова Педагогічної ради, директор \underline{\hspace{3cm}}~О.В.Собчук\\
\end{minipage}
\end{flushright}

\begin{flushright}
\begin{minipage}{9.5cm}
Освітньо-професійна програма вводиться в дію з \underline{\hspace{2cm}} 20\underline{\hspace{0.7cm}}~р.\\
Ректор \underline{\hspace{3cm}}~Р.І.~Петришин\\
(наказ №\underline{\hspace{0.7cm}} від <<\underline{\hspace{0.7cm}}>> \underline{\hspace{2cm}}  20\underline{\hspace{0.7cm}}~р.)\\
\end{minipage}
\end{flushright}
\vfill
\begin{center}
Чернівці, 2022
\end{center}
        \end{titlepage}
\begin{titlepage}
\begin{center}
ЛИСТ ПОГОДЖЕННЯ\\
освітньо-професійної програми
\end{center}


ГАЛУЗЬ ЗНАНЬ \galuz

СПЕЦІАЛЬНІСТЬ \spec

КВАЛІФІКАЦІЯ фаховий молодший бакалавр з комп’ютерних наук 

\vspace{1cm}
\begin{tabular}{p{8cm}p{8cm}}
\begin{flushleft}
\begin{minipage}{8cm}
<<РОЗРОБЛЕНО>>\\
Робочою групою ВСП <<Фаховий коледж ЧНУ>>\\
Керівник робочої групи\\
\underline{\hspace{3cm}}~В.В.~Ковдриш\\


\vspace{0.5cm}

<<СХВАЛЕНО>>\\
Цикловою комісією комп'ютерних наук ВСП <<Фаховий коледж ЧНУ>>, голова циклової комісії\\
\underline{\hspace{3cm}}~В.В.~Коропецький\\
%<<\underline{\hspace{1cm}}>> \underline{\hspace{3cm}} 2018 р.\\
Протокол №\underline{\hspace{0.5cm}} від <<\underline{\hspace{0.5cm}}>> \underline{\hspace{1cm}}  20\underline{\hspace{0.5cm}}~р.\\

\vspace{0.5cm}

<<СХВАЛЕНО>>\\
Методичною радою ВСП <<Фаховий коледж ЧНУ>>\\
Голова Методичної ради\\
\underline{\hspace{3cm}}~О.Я.~Білокрила\\
%<<\underline{\hspace{1cm}}>> \underline{\hspace{3cm}} 2018 р.\\
Протокол №\underline{\hspace{0.5cm}} від <<\underline{\hspace{0.5cm}}>> \underline{\hspace{1cm}}  20\underline{\hspace{0.5cm}}~р.\\
\end{minipage}
\end{flushleft}
&
\begin{flushright}
\begin{minipage}{8cm}
<<ПОГОДЖЕНО>>\\
Начальник навчального відділу Чернівецького національного університету імені Юрія Федьковича\\
\underline{\hspace{3cm}}~Я.Д.~Гарабажів\\


\vspace{0.5cm}

<<РЕКОМЕНДОВАНО>>\\
Комісією Вченої ради з навчально-методичної роботи Чернівецького національного університету імені Юрія Федьковича\\
Голова комісії з навчально-методичної роботи\\
\underline{\hspace{3cm}}~О.В.~Мартинюк\\
%<<\underline{\hspace{1cm}}>> \underline{\hspace{3cm}} 2018 р.\\
Протокол №\underline{\hspace{0.5cm}} від <<\underline{\hspace{0.5cm}}>> \underline{\hspace{1cm}}  20\underline{\hspace{0.5cm}}~р.\\
\end{minipage}
\end{flushright} \\
\end{tabular}

\end{titlepage}
        \clearpage
        \pagenumbering{arabic}

        ''',
}
latex_logo = '_static/KN.jpg'
latex_show_urls = 'footnote'
