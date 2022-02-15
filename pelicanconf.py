#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'root'
SITENAME = 'Fighting the System'
SITESUBTITLE = 'A blog of hacks and workarounds'
SITEURL = 'https://brashear.me'

# Use Octopress URL structure.
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'

DEFAULT_CATEGORY = 'Blog'

# Clean the output directory each time we regenerate the site
#DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images','files','extras',]
EXTRA_PATH_METADATA = {
	'extras/robots.txt': {'path': 'robots.txt'},
	'extras/z8e6yosgc.txt': {'path': 'z8e6yosgc.txt'},
	'extras/.htaccess': {'path': '.htaccess'},
}

THEME = 'themes/pelican-feather'

# Plugin settings
PLUGIN_PATHS = ['plugins\sitemap\pelican\plugins']
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
#RELATIVE_URLS = True
