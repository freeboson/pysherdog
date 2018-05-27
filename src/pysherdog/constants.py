#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018, Sujeet Akula <sujeet@freeboson.org>
# Distributed under terms of the MIT license.

"""
Global constants
"""

from urllib.parse import urljoin
from pysherdog import __version__

USER_AGENT = f'Mozilla/5.0 pysherdog/{__version__}'
HEADERS = {'User-Agent': USER_AGENT}
SHERDOG_BASE_URL = 'https://www.sherdog.com/'
SHERDOG_FIGHTER_URL = urljoin(SHERDOG_BASE_URL, 'fighter/')

