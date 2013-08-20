#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admalledd'
SITENAME = u"admalledd's notes"
SITEURL = ''

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),

          ('Jinja2', 'http://jinja.pocoo.org/'),)
# Social widget
SOCIAL = (('Twitter: @admalledd', 'http://twitter.com/admalledd'),
          ('Email: admalledd@gmail.com', 'mailto://admalledd@gmail.com'),)

DEFAULT_PAGINATION = 10


MD_EXTENSIONS = [
                'fenced_code',
                'codehilite(force_linenos=True,noclasses=False,pygments_style=native)',
                'tables',
                'extra'
               ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
