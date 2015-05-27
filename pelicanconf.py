#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Jonsson'
SITENAME = 'jonsson.ninja'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

# Feed
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME='pelican-svbhack'
USER_LOGO_URL=SITEURL + '/images/bio-photo.jpg'
TAGLINE='Swedish software engineering student.'

# URL
ARCHIVES_SAVE_AS = 'posts/index.html'
ARCHIVES_URL = 'posts/'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''


# Blogroll
LINKS = (
    ('My portfolio', 'http://matachi.se/'),
)

# Social widget
SOCIAL = (
    ('Email', 'mailto:daniel@jonsson.xyz'),
    ('Twitter', 'https://twitter.com/DanielJonss'),
    ('Github', 'https://github.com/matachi'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
