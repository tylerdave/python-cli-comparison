#!/usr/bin/env python
from __future__ import print_function
"""Example CLI program using [package/module]."""

# import [package/module]


def cli():
    """CLI program entry point."""
    parsed_arguments = {}
    parsed_arguments['positional'] = ''
    parsed_arguments['optional'] = ''
    parsed_arguments['flag'] = ''

    print(parsed_arguments)

if __name__ == '__main__':
    cli()
