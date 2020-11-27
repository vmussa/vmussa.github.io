#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://vmussa.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "G-BD2LTYCV4K"
# GOOGLE_ADSENSE = {
#     'ca_id': 'ca-pub-3187686650481081',
#     'page_level_ads': True,          # Allow Page Level Ads (mobile)
#     'ads': {
#         'aside': '1234561',          # Side bar banner (all pages)
#         'main_menu': '1234562',      # Banner before main menu (all pages)
#         'index_top': '1234563',      # Banner after main menu (index only)
#         'index_bottom': '1234564',   # Banner before footer (index only)
#         'article_top': '1234565',    # Banner after article title (article only)
#         'article_bottom': '1234566', # Banner after article content (article only)
#     }
# }
GOOGLE_TAG_MANAGER = 'GTM-NNQ7JK3'