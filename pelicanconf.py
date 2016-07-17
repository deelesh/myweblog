#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Deelesh Mandloi'
SITENAME = u'My Weblog'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_METADATA = {
    'status': 'published',
}

TYPOGRIFY = True

#Settings for processing markdown files
MD_EXTENSIONS = ['extra', 'toc', 'fenced_code', 'codehilite(css_class=highlight)']

# Settings specific to notmyidea default theme
#GITHUB_URL = 'https://github.com/deelesh'
#MENUITEMS = (('Blog', '/'),
#            )
DISQUS_SITENAME = 'deelesh'

# Settings for elegant theme
THEME = "pelican-themes/elegant"
LANDING_PAGE_ABOUT = {
    'title': 'My Weblog',
    'details': '''I am Deelesh Mandloi. I work as a Product Engineer in the software development group at <a href="http://www.esri.com">Esri</a> building geocoding and routing    services available with <a href="http://www.arcgis.com">ArcGIS Online</a>. I love Geography, maps, and writing code in Python. This is my personal blog. The views and opinions expressed on this blog are my own and do not necessarily represent those of my employer.'''
}
COMMENTS_INTRO = u'Any suggestions or feedback? Leave your comments below.'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Python Module of the Week', 'http://pymotw.com/'),
#         ('Planet Python', 'http://planetpython.org/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/deelesh'),
          ('twitter', 'http://twitter.com/deelesh'),
           ('Email', 'mailto:deelesh@gmail.com'),
         )
TWITTER_USERNAME = "deelesh"

DEFAULT_PAGINATION = 8

#Pelican Plugins
PLUGINS = ['pelican_gist', 'extract_toc', 'tipue_search', 'neighbors', 'share_post']
PLUGIN_PATHS = ['pelican-plugins/', 'pelican-plugins/pelican-gist']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
