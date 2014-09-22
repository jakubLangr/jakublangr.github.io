#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jakub Langr'
SITENAME = u"Jakub Langr's Blog"
SITEURL = ''
THEME = "pelican-themes/svbtle"

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'en'

# Social widget
SOCIAL =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),)

# Blogroll
LINKS = (('LinkedIn', 'http://linkedin.com/in/jakublangr'),
          ('GitHub', 'https://github.com/jakubLangr'),
          ('Mail','mailto:james.langr@gmail.com'),
          ('About', '/about.html'))

DEFAULT_PAGINATION = 10

DEFAULT_DATE_FORMAT = ('%d/%m/%Y')

GOOGLE_ANALYTICS = 'UA-55040887-1'
GOOGLE_ANALYTICS_DOMAIN = 'jakublangr.com'

DISQUS_SITENAME = 'jakublangr'


'''

### SPECIFIC TO BT3 FLAT

TEMPLATE_PAGES = {'blog.html': 'blog.html'}

# Do not publish articles set in the future
WITH_FUTURE_DATES = False
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

SWIFTYPE = ''
SITE_THUMBNAIL = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
SITE_THUMBNAIL_TEXT = "Jakub Langr's Blog"
SITESUBTITLE = 'About data and all things awesome'


### Plugin-specific settings

RELATED_POSTS_MAX = 20

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


RELATIVE_URLS = True



#===theme settings===========================

FAVICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
SHORTCUT_ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'

# About ME
PERSONAL_PHOTO = "https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-xaf1/v/t1.0-9/524390_3116109135262_1020257129_n.jpg?oh=0cff8cc42ef25e6edf37ad9d5f895764&oe=5489085E&__gda__=1419142713_c676c016b2f5fef4707be7b7a39daffa"
PERSONAL_INFO = """I am a final year undergraduate at University of Oxford studying mostly economics, but really just spending loads of time on Coursera and similar awesome MOOC sites (I mean, I have to love them, I already finished 12 courses...) playing with machine learning, data science, statistics, computer science and all the things awesome.

I love to hack data and I worked in a data science position for a half a year at Pearson Plc, but I also have full-time like experience from international consultancies and NGOs. 

If you want to, feel free to get in touch via any of the social widgets. """

# work
# WORK_DESCRIPTION = ''
# items to descripe a work, "type", "cover-image link", "title", "descption", "link"

'''