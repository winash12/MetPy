#!/usr/bin/env python3
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import datetime
import os
from pathlib import Path
import re
import sys

import metpy

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use resolve() to make it absolute, like shown here.
cwd = Path.cwd().resolve()
sys.path.insert(0, str(cwd))
sys.path.insert(0, str(cwd.parent.parent))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '2.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design',
    'sphinx_gallery.gen_gallery',
    'matplotlib.sphinxext.plot_directive',
    'myst_parser',
    'make_areas'
]

sphinx_gallery_conf = {
    'doc_module': ('metpy',),
    'reference_url': {
        'metpy': None,
    },
    'examples_dirs': [str(cwd.parent / 'examples'), str(cwd.parent / 'tutorials')],
    'gallery_dirs': ['examples', 'tutorials'],
    'filename_pattern': r'\.py',
    'backreferences_dir': str(Path('api') / 'generated'),
    'default_thumb_file': str(Path('_static') / 'metpy_150x150_white_bg.png'),
    'abort_on_example_error': True,
    'reset_modules': [lambda conf, fname: sys.modules.pop('pint', None)]
}

# By default, only generate all the areas when running in CI
metpy_generate_all_areas = 'GITHUB_ACTIONS' in os.environ

# Turn off code and image links for embedded mpl plots
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ['png']
plot_rcparams = {'savefig.bbox': 'tight'}

# Make MyST generate anchors for headings
myst_heading_anchors = 2

# Set up mapping for other projects' docs
intersphinx_mapping = {
                       'cartopy': ('https://scitools.org.uk/cartopy/docs/latest/', None),
                       'matplotlib': ('https://matplotlib.org/stable/', None),
                       'numpy': ('https://numpy.org/doc/stable/', None),
                       'pandas': ('https://pandas.pydata.org/docs/', None),
                       'pint': ('https://pint.readthedocs.io/en/stable/', None),
                       'pyproj': ('https://pyproj4.github.io/pyproj/stable/', None),
                       'python': ('https://docs.python.org/3/', None),
                       'scipy': ('https://docs.scipy.org/doc/scipy/', None),
                       'xarray': ('https://docs.xarray.dev/en/stable/', None)
                       }

nitpicky = True
nitpick_ignore = [
    ('py:class', 'M'), ('py:class', 'N'), ('py:class', 'P'), ('py:class', '2'),
    ('py:class', 'optional'), ('py:class', 'array-like'), ('py:class', 'file-like object'),
    # For traitlets docstrings
    ('py:class', 'All'), ('py:class', 'callable'),
    # Next two are from Python dict docstring that we inherit
    ('py:class', 'a shallow copy of D'),
    ('py:class', 'v, remove specified key and return the corresponding value.')
]

nitpick_ignore_regex = [
    ('py:class', r'default:.*'),  # For some traitlets docstrings
    ('py:class', r'.*object providing a view on.*'),  # Python dict docstring
    ('py:class', r'None.  .*'),  # Python dict docstring
    ('py:class', r'.*D\[k\].*'),  # Python dict docstring
]

# Tweak how docs are formatted
napoleon_use_rtype = False

# Control main class documentation
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

# Controlling automatically generating summary tables in the docs
autosummary_generate = True
autosummary_ignore_module_all = False

# The encoding of source files.
# source_encoding = 'utf-8-sig'
cur_date = datetime.utcnow()

# The main toctree document.
master_doc = 'index'

# General information about the project.
project = 'MetPy'

# noinspection PyShadowingBuiltins
copyright = (
    f'2008\u2013{cur_date:%Y}, MetPy Developers.'
    'Development is supported by Unidata and the National Science Foundation.'
)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
verinfo = metpy.__version__
parsed_version = re.search(r'(?P<full>(?P<base>\d+\.\d+)\.?\w*)', verinfo).groupdict()
# The short X.Y version.
version = parsed_version['base']
if '+' in verinfo:
    version += 'dev'
# The full version, including alpha/beta/rc tags.
release = parsed_version['full']

rst_prolog = f'''
.. |cite_version| replace:: {release}
.. |cite_year| replace:: {cur_date:%Y}
.. |access_date| replace:: {cur_date:%d %B %Y}
'''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'autolink'

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    'external_links': [
        {'name': 'Release Notes', 'url': 'https://github.com/Unidata/MetPy/releases'},
    ],
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/Unidata/MetPy',
            'icon': 'fa-brands fa-github-square',
            'type': 'fontawesome',
        },
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/MetPy',
            'icon': 'fa-brands fa-twitter-square',
            'type': 'fontawesome',
        }
    ],
    'use_edit_page_button': False,
    'analytics': {'google_analytics_id': 'G-J48T2BG3J7'},
    'navbar_align': 'left',
    'navbar_start': ['navbar-logo', 'version-switcher'],
    'navbar_center': ['navbar-nav'],
    'header_links_before_dropdown': 6,
    'navbar_persistent': ['search-button'],
    'navbar_end': ['navbar-icon-links', 'theme-switcher'],
    'switcher': {
        'json_url': 'https://unidata.github.io/MetPy/pst-versions.json',
        'version_match': 'dev' if 'dev' in version else version,
    },
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {'canonical_url': 'https://unidata.github.io/MetPy/latest/'}

# Extra variables that will be available to the templates. Used to create the
# links to the Github repository sources and issues
html_context = {
    'doc_path': 'docs',
    'galleries': sphinx_gallery_conf['gallery_dirs'],
    'gallery_dir': dict(zip(sphinx_gallery_conf['gallery_dirs'],
                            sphinx_gallery_conf['examples_dirs'])),
    'api_dir': 'api/generated',
    'github_user': 'Unidata',
    'github_repo': 'MetPy',
    'github_version': 'main',  # Make changes to the main branch
    'default_mode': 'light',
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = ' '.join((project, version))

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = str(Path('_static') / 'metpy_horizontal.png')

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = str(Path('_static') / 'metpy_32x32.ico')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['theme-unidata.css']
html_js_files = ['doc_shared.js']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y at %H:%M:%S'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['sidebar-nav-bs']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'MetPydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'MetPy.tex', 'MetPy Documentation',
   'MetPy Developers', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'metpy', 'MetPy Documentation',
     ['MetPy Developers'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'MetPy', 'MetPy Documentation',
   'MetPy Developers', 'MetPy', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# -- Options for linkcheck builder ----------------------------------------

# List of regular expressions, links matching them will be ignored.
linkcheck_ignore = [
    r'https://codecov.io/github/Unidata/MetPy',
    r'https://www\.youtube\.com/watch\?v=[\d\w\-_]+',
    r'https://youtu\.be/[\d\w\-_]+',
    # Giving 404s right now and is not going to change
    r'https://twitter\.com/MetPy',
    # AMS DOIs should be stable, but resolved link consistently 403's with linkcheck
    r'https://doi\.org/10\.1175/.*',
    # This one appears to be blocking robots
    r'https://doi\.org/10\.1088/0026-1394/45/2/004',
    # Frequently fails the linkchecker
    r'https://ams\.confex\.com/ams/[\d\w]+/meetingapp\.cgi/.*',
    # Can't seem to get around inconsistent retry errors
    r'https://doi\.org/10\.1289/ehp\.1206273',
    # Couldn't fix these 403's with user agents
    r'https://doi\.org/10\.1029/2010GL045777',
    r'https://doi\.org/10\.1098/rspa\.2004\.1430'
    ]

# Dictionary of URL redirects allowed
linkcheck_allowed_redirects = {
    r'https://pint\.readthedocs\.io': r'https://pint\.readthedocs\.io/en/stable/',
    r'https://conda.io/docs/': r'https://conda.io/en/latest/',
    r'https://github.com/Unidata/MetPy/issues/new/choose': r'https://github.com/login.*choose',
    r'https://doi.org/.*': r'https://.*',
    r'https://gitter.im/Unidata/MetPy': r'https://app.gitter.im/.*MetPy.*'
}

# Domain-specific HTTP headers for requests
linkcheck_request_headers = {
    r'https://docs.github.com/': {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; '
                                                'rv:24.0) Gecko/20100101 Firefox/24.0'}
}
