# Configuration file for the Sphinx documentation builder for
# matplotlib projects.

# Release mode enables optimizations and other related options.
is_release_build = tags.has('release')  # noqa

# -- Project information -----------------------------------------------------

project = "Matplotlib Sphinx Theme"
copyright = "2021, Matplotlib Contributors"
author = "Matplotlib Contributors"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "mpl_sphinx_theme"
html_logo = "_static/logo2.svg"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "logo_link": "https://matplotlib.org/stable/",
    # collapse_navigation in pydata-sphinx-theme is slow, so skipped for local
    # and CI builds https://github.com/pydata/pydata-sphinx-theme/pull/386
    "collapse_navigation": not is_release_build,
    "icon_links": [
        {
            "name": "gitter",
            "url": "https://gitter.im/matplotlib",
            "icon": "fab fa-gitter",
        },
        {
            "name": "discourse",
            "url": "https://discourse.matplotlib.org",
            "icon": "fab fa-discourse",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/matplotlib/matplotlib",
            "icon": "fab fa-github-square",
        },
        {
            "name": "twitter",
            "url": "https://twitter.com/matplotlib/",
            "icon": "fab fa-twitter-square",
        },
    ],
    "show_prev_next": False,
    "navbar_center": ["mpl_nav_bar.html"],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["static"]