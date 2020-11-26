#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Vítor Mussa'
SITENAME = 'Ciência de Dados e Sociologia Computacional e Digital por Vítor Mussa'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('página inicial', 'https://vmussa.github.io/'),
         ('portfólio', '#'),
         ('tutoriais', '#'),)

# Social widget
SOCIAL = (('Github', '#'),
          ('Twitter', '#'),
          ('LinkedIn', '#'),
          ('Lattes', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = '..\\pelican-themes\\Flex\\'

# Analytics & Monetization
GOOGLE_ANALYTICS = 'G-BD2LTYCV4K'
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-3187686650481081',
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}
