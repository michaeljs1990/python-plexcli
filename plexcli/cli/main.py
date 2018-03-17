"""
Main class to hold all of the logic around commands and flags.
Click should never be used outside of this file to make us
relatively agnostic about what lib we use for the cli.
"""
import sys
import click
import logging
from os import path
from pathlib import Path as pathlib


@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--config', default='')
@click.pass_context
def cli(ctx, verbose, config):
    ctx.obj = {}
    ctx.obj['verbose'] = verbose

    # Setup logger that pipes to stdout
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',  # noqa: E501
        handlers=[logging.StreamHandler(sys.stdout)]
    )

    logger = logging.getLogger("plexcli")
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    if config == '':
        ctx.obj['config'] = path.join(str(pathlib.home()), ".plex.yaml")
    else:
        ctx.obj['config'] = config

    logger.info("config path set to %s" % ctx.obj['config'])


@cli.command()
@click.pass_context
def something(ctx):
    l = logging.getLogger("plexcli")
    l.warning("WARNING")
    l.info("INFO")
    pass
