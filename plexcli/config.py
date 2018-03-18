"""
    Load in all config needed to make further requests. Following
    is an example of all currently supported keys in the config
    file that should be located at $HOME/.plex.yaml

    ---
    host: http://localhost:9090
    user: example
    pass: password
    token: 1234abdc
"""
import sys
import yaml


class PlexCliConfig(object):

    def __init__(self, path, logger):
        self.logger = logger
        self.path = path
        conf = self.load_yaml()
        self.parse_yaml(conf)

    def load_yaml(self):
        """
        Load yaml file into memory
        """
        try:
            fd = open(self.path, "r")
            return yaml.safe_load(fd)
        except FileNotFoundError as e:
            self.logger.fatal("Unable to load %s" % self.path)
            sys.exit(1)

    def parse_yaml(self, conf):
        """
        Set all keys that are valid in yaml and then run some
        sanity checks to ensure we will be able to make an
        api call... i.e. password and token aren't missing.
        """
        self.host = conf['host'] if 'host' in conf else None
        self.user = conf['user'] if 'user' in conf else None
        self.password = conf['pass'] if 'pass' in conf else None
        self.token = conf['token'] if 'token' in conf else None

        if self.password is None and self.token is None:
            self.logger.fatal("No password or token is set in %s" % self.path)
            sys.exit(1)

        if self.host is None:
            self.logger.fatal("No host is set in %s" % self.path)
            sys.exit(1)

        if self.user is None:
            self.logger.fatal("No user is set in %s" % self.path)
            sys.exit(1)
