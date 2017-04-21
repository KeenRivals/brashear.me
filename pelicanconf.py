#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'root'
SITENAME = 'Fighting the System'
SITEURL = ''

PATH = 'content'

DEFAULT_CATEGORY = 'Blog'

# Clean the output directory each time we regenerate the site
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images','files']

THEME = 'themes/feather'

# Plugin settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

# Sitemap settings
SITEMAP = { 'format': 'xml' }

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
