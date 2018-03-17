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


class PlexCliConfig(object):

    def __init__(self, path):
        self.path = path
