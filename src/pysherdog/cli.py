#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018, Sujeet Akula <sujeet@freeboson.org>
# Distributed under terms of the MIT license.

import argparse
import sys
import pysherdog.fighter


def cli_parser():
    handlers = {}
    parsers = {}
    parser = argparse.ArgumentParser(
        description='Query and extract data from Sherdog')

    subparsers = parser.add_subparsers(metavar='subcommand', dest='subcommand')
    subparsers.required = True

    pysherdog.fighter.cli_parser(subparsers, handlers, parsers)

    return parser, handlers, parsers


def main(args=None):
    parser,handlers,parsers = cli_parser()
    args = parser.parse_args(args=args)
    sys.exit(handlers[args.subcommand](args, parsers[args.subcommand]))

