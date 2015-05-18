#!/usr/bin/env python
from __future__ import print_function
"""Example CLI program using docopt."""

from docopt import docopt

USAGE = """Example Docopt CLI Program

Usage:
  docopt_cli.py <positional_arg> [--optional-arg=<optional_arg>] [--flag]
  docopt_cli.py (-h | --help)
  docopt_cli.py --version

Options:
    -h --help                       Show this help screen.
    --version                       Show version.
    -o <optional_arg>, --optional-arg=<optional_arg>   An optional argument.
    --flag                          A boolean argument.
"""

def cli():
    """CLI program entry point."""
    args = docopt(USAGE, version='Docopt CLI Example 0.1')

    parsed_arguments = {}
    parsed_arguments['positional'] = args['<positional_arg>']
    parsed_arguments['optional'] = args['--optional-arg']
    parsed_arguments['flag'] = args['--flag']

    print(parsed_arguments)


if __name__ == '__main__':
    cli()
