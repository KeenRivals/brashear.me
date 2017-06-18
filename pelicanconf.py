#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'root'
SITENAME = 'Fighting the System'
SITESUBTITLE = 'A blog of hacks and workarounds'
SITEURL = 'https://brashear.me'

PATH = 'content'

DEFAULT_CATEGORY = 'Blog'

# Clean the output directory each time we regenerate the site
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images','files']

THEME = 'themes/pelican-feather'

# Plugin settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

# Sitemap settings
SITEMAP = { 'format': 'xml' }

TIMEZONE = 'America/New_York'
DEFAULT_DATE_Format = '%b %D, %Y'
DATE_FORMATS = {
	'en': '%b %d, %Y',
}


DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
	('Email','mailto:web@brashear.me'),
	('GitHub','https://github.com/KeenRivals')
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
