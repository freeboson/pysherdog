#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018, Sujeet Akula <sujeet@freeboson.org>
# Distributed under terms of the MIT license.

"""
Boilerplate, and wrapping tools
"""

import posixpath
from urllib.parse import urlparse
from functools import singledispatch
from datetime import datetime


def get_soup(soup, args):
    if soup is not None:
        return soup.find(*args)


def get_soups(soup, args):
    if soup is not None:
        return soup.find_all(*args)
    return []


def safe_get_str(e):
    return getattr(e, 'string', None)


def get_canonical_id(url):
    """ Tail of path attr of parsed URL is the canonical id """
    parsed = urlparse(url)
    (_, canonical_id) = posixpath.split(parsed.path)
    return canonical_id


@singledispatch
def json_serialize(obj):
    """ Default serialization. Just fail.  """
    raise TypeError(f"{type(obj)} no extra serializer for this type")


@json_serialize.register(datetime)
def _(dt):
    return dt.isoformat()

