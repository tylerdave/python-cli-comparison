#!/usr/bin/env python
from __future__ import print_function
"""Example CLI program using click."""

import click

@click.command()
@click.option('--optional-arg', default='option default',
        help='an optional argument')
@click.option('--flag', is_flag=True)
@click.argument('positional_arg')
def cli(positional_arg, optional_arg, flag):
    """CLI program entry point."""

    parsed_arguments = {}
    parsed_arguments['positional'] = positional_arg
    parsed_arguments['optional'] = optional_arg
    parsed_arguments['flag'] = flag

    print(parsed_arguments)

if __name__ == '__main__':
    cli()
