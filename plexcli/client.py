"""
    Base client used for communicating with the plex api
"""
from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount


class PlexCliClient(object):

    def __init__(self, conf):
        """
        conf needs to be a PlexCliConf object
        """
        self.client = self.init_client(conf)

    def init_client(self, conf):
        """
        Create a http client for plex based on a
        password or token depending on conf file.
        If both are set we use the password.
        """
        if conf.password is not None:
            account = MyPlexAccount(conf.user, conf.password)
            return account.resource(conf.host).connect()
        else:
            return PlexServer(conf.host, conf.token)
