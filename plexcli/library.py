"""
    Class to interact with the plex library api
"""


class PlexCliLibrary(object):

    def __init__(self, api):
        self.client = api.client
        self.list_clients()

    def list_clients(self):
        """
        List all clients that are connected to the server.
        """
        for client in self.client.clients():
            print(client.title)
