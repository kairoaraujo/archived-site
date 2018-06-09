#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Kairo Araujo'
SITENAME = 'Kairo Araujo'
SITESUBTITLE = "Python, automation, infrastructure, AIX, PowerVM, Linux, etc"
SITEURL = 'https://kairo.eti.br'
GITHUB_URL = 'http://github.com/kairoaraujo'
TWITTER_URL = 'http://twitter.com/kairoaraujo'
LINKEDIN_URL = 'https://linkedin.com/in/kairoaraujo'
FACEBOOK_URL = 'http://facebook.com/araujo.kairo'
DISQUS_SITENAME = u'kairoaraujo'
GOOGLE_ANALYTICS = 'UA-108092336-1'
HEADER_COVER = 'static/dc.jpg'

PATH = 'content'
STATIC_PATHS = ['static', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ''

# Social widget
SOCIAL = (('LinkedIn', LINKEDIN_URL),
          ('GitHub', GITHUB_URL),
          ('Twitter', TWITTER_URL),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Footer included
FOOTER_INCLUDE = 'extras/myfooter.html'
IGNORE_FILES = [FOOTER_INCLUDE]
EXTRA_TEMPLATES_PATHS = [os.path.dirname(__file__)]

THEME = u'themes/pelican-clean-blog'
