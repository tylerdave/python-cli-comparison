#!/usr/bin/env python
from __future__ import print_function
"""Example CLI program using argparse."""

import argparse

ARGUMENTS = {}


def cli():
    """CLI program entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('positional_arg', help='a positional argument')
    parser.add_argument('-o', '--optional-arg', default='default value',
            help='an optional argument')
    parser.add_argument('-f', '--flag', action='store_true',
            help='a binary flag')
    args = parser.parse_args()

    ARGUMENTS['positional'] = args.positional_arg
    ARGUMENTS['optional'] = args.optional_arg
    ARGUMENTS['flag'] = args.flag

    print(ARGUMENTS)

if __name__ == '__main__':
    cli()
