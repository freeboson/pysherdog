#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018, Sujeet Akula <sujeet@freeboson.org>
# Distributed under terms of the MIT license.

"""
Fighter models and queries
"""

import urllib.request
from urllib.parse import urljoin
import posixpath
import json
from bs4 import BeautifulSoup
import dateutil.parser
from pysherdog.errors import UnknownFighter
from pysherdog.constants import USER_AGENT
from pysherdog.constants import SHERDOG_FIGHTER_URL
from pysherdog.parse.fighter import *
from pysherdog.util import get_soup,\
                           get_soups,\
                           safe_get_str,\
                           get_canonical_id,\
                           json_serialize


def cli_parser(subparsers, handlers, parsers):
    subcommand = 'fighter'
    handlers[subcommand] = main
    parser = subparsers.add_parser(
        subcommand,
        help='Get fighter data',
        description='Extract all data on a given fighter')
    parser.add_argument('-t', '--timeout', help='timeout in seconds')
    parser.add_argument('-u', '--user_agent', help='user agent string')
    parser.add_argument('-p', '--parser', help='bs4 parser')
    parser.add_argument('fighter_id', help='Sherdog fighter ID')

    parser.set_defaults(timeout=None, user_agent=USER_AGENT, parser='lxml')

    parsers[subcommand] = parser


def main(args, parser):
    try:
        data = get_fighter(args.fighter_id,
                           ua=args.user_agent,
                           timeout=args.timeout,
                           parser=args.parser)
        print(json.dumps(data, indent=4, default=json_serialize), end="\n\n")
        return 0
    except UnknownFighter:
        print("Could not find fighter in Sherdog.")
        return 1
    except:
        print("Unknown error")
        raise


def get_fighter(fighter_id_query, ua=USER_AGENT, timeout=None, parser='lxml'):
    """
    Pull information of a fighter given their sherdog ID
    """
    resp = load_fighter(fighter_id_query, ua, timeout)
    fighter_id = get_canonical_id(resp.geturl())
    data = parse_data(resp.read(), parser)
    return data


def parse_data(html, parser):
    """
    Handle all the parsing of the raw HTML
    """
    soup = BeautifulSoup(html, parser)
    bio = get_soup(soup, BIO)

    name = safe_get_str(get_soup(bio, NAME))
    nick = safe_get_str(get_soup(bio, NICKNAME))
    nationality = safe_get_str(get_soup(bio, NATIONALITY))
    locality = safe_get_str(get_soup(bio, LOCALITY))
    birth_date = safe_get_str(get_soup(bio, BIRTH_DATE))
    birth_date_dt = (dateutil.parser.parse(birth_date)
                     if birth_date is not None
                     else None)

    assoc_parent = get_soup(bio, ASSOCIATION_PARENT)
    association = safe_get_str(get_soup(assoc_parent, ASSOCIATION))

    wc_parent = get_soup(bio, WEIGHT_CLASS_PARENT)
    weight_class = safe_get_str(get_soup(wc_parent, WEIGHT_CLASS))

    sz = get_soup(bio, SIZE_INFO)
    wt_parent = get_soup(sz, WEIGHT_PARENT)
    ht_parent = get_soup(sz, HEIGHT_PARENT)
    weight = safe_get_str(get_soup(wt_parent, WEIGHT))
    height = safe_get_str(get_soup(ht_parent, HEIGHT))

    record = get_soup(bio, RECORD)
    bio_graphs = get_soups(record, BIO_GRAPH)
    stats = parse_record(bio_graphs)

    fight_histories = parse_histories(get_soups(soup, FIGHT_HISTORY))

    return {
        'name': name,
        'nick': nick,
        'nationality': nationality,
        'locality': locality,
        'birth_date': birth_date_dt,
        'association': association,
        'weight_class': weight_class,
        'height': height,
        'weight': weight,
        **stats,
        **fight_histories
    }


def parse_histories(histories):
    fight_histories = {
        'fights': [],
        'amateur_fights': [],
    }
    for hist in histories:
        ev_type = ('fights'
                   if 'pro' in hist.h2.text.lower()
                   else 'amateur_fights')
        for evt in get_soups(hist, HISTORY_ROW):
            cols = evt.find_all('td')
            if len(cols) != 6:
                continue
            fight_histories[ev_type].append({
                'result': safe_get_str(cols[0]),
                'opponent': safe_get_str(cols[1]),
                'opponent_id': get_canonical_id(cols[1].a['href']),
                'event': safe_get_str(cols[2].span),
                'event_id': get_canonical_id(cols[2].a['href']),
                'event_date': dateutil.parser.parse(
                    safe_get_str(get_soup(cols[2], SUB_LINE))),
                'method': cols[3].text.split(cols[3].span.text)[0],
                'referee': safe_get_str(cols[3].span),
                'round': safe_get_str(cols[4]),
                'time': safe_get_str(cols[5]),
            })
    return fight_histories


def parse_record(bio_graphs):
    record = {}
    for bg in bio_graphs:
        category = RECORD_CATEGORIES[safe_get_str(get_soup(bg, RESULT))]
        cnt = safe_get_str(get_soup(bg, COUNTER))
        total = int(cnt) if cnt is not None else None
        if category == 'ncs':
            record[category] = total
        else:
            results = {
                RESULT_TYPES[rt]: n
                for rt,n in map(parse_result,
                                get_soups(bg, GRAPH_TAG))
            }
            record[category] = {
                'total': total,
                **results
            }
    return record


def parse_result(tag):
    [n, rt, _] = tag.text.split(' ')
    return (rt, int(n))


def load_fighter(fighter_id_query, ua, timeout):
    """ Perform the get """
    headers = {'User-Agent': ua}
    url = urljoin(SHERDOG_FIGHTER_URL, fighter_id_query)
    req = urllib.request.Request(url=url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
    except urllib.request.HTTPError:
        raise UnknownFighter

    fighter_id = get_canonical_id(resp.geturl())
    return resp

