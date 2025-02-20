# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'AIMMS Function Reference'
copyright = u'2020, AIMMS B.V.'
author = u'AIMMS'
# changes format of date on the home page
today_fmt = '%B, %Y'

book_title = "Function Reference"

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.builders.linkcheck',
    'sphinx_aimms_theme',
]

if os.name != 'nt':

    #Imports sitemap extension to build the sitemap automatically
    extensions.append('sphinx_sitemap')
    html_baseurl = "https://documentation.aimms.com/functionreference/"
    extensions.append('sphinx_last_updated_by_git')

intersphinx_mapping = {'howto': ('https://how-to.aimms.com/', None),
                       'lr': ('https://documentation.aimms.com/language-reference', None),
                       'docs': ('https://documentation.aimms.com', None)}

# A list of regular expressions that match URIs that should not be checked when doing a linkcheck build.   
linkcheck_ignore = [r'https://web.imt-atlantique.fr/x-info/sdemasse/gccatold/titlepage.html',
                    r'https://www.gurobi.com/documentation/9.1/refman/configuration_parameters.html',
                    r'https://www.gurobi.com/documentation/9.1/refman/parameters.html#sec:Parameters']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'aimmslexer'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_aimms_theme'

if os.name == 'nt':
   
   Display_edit_on_gitlab = True
   # if builds locally (a windows machine), do not displays external extensions (Google Analytics, Community Embeddable, Algolia search, etc.)
   Display_3rd_Party_Extensions = False
else:

   # if builds on GitLab (a Linux machine), force "Edit on Gitlab" not to be shown, and displays external extensions (Google Analytics, Community Embeddable, Algolia search, etc.)
   Display_edit_on_gitlab = False
   Display_3rd_Party_Extensions = True


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme_options = {

    'doc_title': 'Function Reference',
    'home_page_title': 'AIMMS Function Reference',
    'home_page_description': 'Find all predeclared AIMMS Language functions and identifiers',
    'display_community_embeddable' : Display_3rd_Party_Extensions,
    'display_local_toc' : False,
    'titles_only' : True,
    'display_algolia_search': False,
    'google_analytics_id': 'UA-1290545-13',
    'generate_google_analytics' : Display_3rd_Party_Extensions,
    'display_help_and_feedback' : True,
    'is_github' : True,
    'repo_url' : "https://github.com/aimms/function-reference",

}

html_last_updated_fmt = '%b %d, %Y'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
# html_context = {
    # 'css_files': ['_static/AIMMS_CodeBlock.css','_static/declaration_icons.css' ] #'_static/custom.css'],
# }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'book-testdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'

my_preamble =  '''
\\usepackage{etoolbox}
\\BeforeBeginEnvironment{fulllineitems}{\\begingroup\\color{white}\\tiny}%
\\AfterEndEnvironment{fulllineitems}{\\endgroup}%
'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    #'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': my_preamble,
    #changes color of internal hyperlinks
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    'sphinxsetup': 'InnerLinkColor={RGB}{203,65,84}, OuterLinkColor={RGB}{0,102,204}',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_doc_name = 'AIMMS_func.tex'

latex_documents = [
    (master_doc, latex_doc_name, book_title,
     u'AIMMS', 'manual', True),
]

latex_logo = "AIMMS_logo_BlackWhite-PRINT-900x508.jpg"

latex_show_pagerefs = True

#latex_show_urls = 'footnote'

#latex_additional_files = ['_fortex/Makefile']


# -- Extension configuration -------------------------------------------------

add_function_parentheses = False
numfig = True

highlight_language = 'aimms'
