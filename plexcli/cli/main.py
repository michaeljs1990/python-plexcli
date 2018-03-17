"""
Main class to hold all of the logic around commands and flags.
Click should never be used outside of this file to make us
relatively agnostic about what lib we use for the cli.
"""
import click


@click.group()
@click.option('--verbose')
def cli(verbose):
    print(verbose)
