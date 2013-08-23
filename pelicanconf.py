#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#THEME = "/home/admalledd/Documents/notes/pelican-themes/cebong"

AUTHOR = u'admalledd'
SITENAME = u"admalledd's website"
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

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('Minecraft Server Information','/pages/mc-index.html'),
             ('FAQ/About me','/pages/faq-about-me.html'),)


#DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
