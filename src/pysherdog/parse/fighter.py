#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018, Sujeet Akula <sujeet@freeboson.org>
# Distributed under terms of the MIT license.

"""
Fighter page parsing constants
"""

BIO = ('div', {'class': 'bio_fighter'})

NAME = ('span', {'class': 'fn'})
NICKNAME = ('span', {'class': 'nickname'})

NATIONALITY = ('strong', {'itemprop': 'nationality'})
LOCALITY = ('span', {'itemprop': 'addressLocality'})
BIRTH_DATE = ('span', {'itemprop': 'birthDate'})

ASSOCIATION_PARENT = ('h5', {'class': 'association'})
ASSOCIATION = ('span', {'itemprop': 'name'})

WEIGHT_CLASS_PARENT = ('h6', {'class': 'wclass'})
WEIGHT_CLASS = ('strong',) # or ('a',)

SIZE_INFO = ('div', {'class': 'size_info'})
WEIGHT_PARENT = ('span', {'class': 'weight'})
WEIGHT = ('strong',)
HEIGHT_PARENT = ('span', {'class': 'height'})
HEIGHT = ('strong',)

RECORD = ('div', {'class': 'record'})
BIO_GRAPH = ('div', {'class': 'bio_graph'})
COUNTER = ('span', {'class': 'counter'})
RESULT = ('span', {'class': 'result'})
GRAPH_TAG = ('span', {'class': 'graph_tag'})

RESULT_TYPES = {
    'KO/TKO': 'knockouts',
    'SUBMISSIONS': 'submissions',
    'DECISIONS': 'decisions',
    'OTHERS': 'others',
}

RECORD_CATEGORIES = {
    'Wins': 'wins',
    'Losses': 'losses',
    'N/C': 'ncs',
}

FIGHT_HISTORY = ('div', {'class': 'fight_history'})
HISTORY_ROW = ('tr', {'class': ['even', 'odd']})
SUB_LINE = ('span', {'class': 'sub_line'})

