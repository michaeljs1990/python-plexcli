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

from plexcli.config import PlexCliConfig
from plexcli.client import PlexCliClient
from plexcli.library import PlexCliLibrary


@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-c', '--config', default='')
@click.pass_context
def cli(ctx, verbose, config):
    # initialize context object because they don't do it for you..
    ctx.obj = {}

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
        config_file = path.join(str(pathlib.home()), ".plex.yaml")
    else:
        config_file = config

    logger.info("config path set to %s" % config_file)

    plex_conf = PlexCliConfig(config_file, logger)
    plex_client = PlexCliClient(plex_conf)
    ctx.obj['config'] = plex_conf
    ctx.obj['client'] = plex_client


@cli.command()
@click.pass_context
def library(ctx):
    PlexCliLibrary(ctx.obj['client'])
