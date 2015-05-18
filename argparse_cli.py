#!/usr/bin/env python
from __future__ import print_function
"""Example CLI program using argparse."""

import argparse


def cli():
    """CLI program entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('positional_arg', help='a positional argument')
    parser.add_argument('-o', '--optional-arg', default='default value',
            help='an optional argument')
    parser.add_argument('-f', '--flag', action='store_true',
            help='a binary flag')
    args = parser.parse_args()

    parsed_arguments = {}
    parsed_arguments['positional'] = args.positional_arg
    parsed_arguments['optional'] = args.optional_arg
    parsed_arguments['flag'] = args.flag

    print(parsed_arguments)

if __name__ == '__main__':
    cli()
