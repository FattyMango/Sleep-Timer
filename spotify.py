import spotipy
from spotipy.oauth2 import SpotifyOAuth


from app_client import *


class Spotify : 
    
    def __init__(self) -> None:
        '''
        Custom class to control Spotify app
         using Spotipy.
                                            '''
        pass

    def create_spotify_auth(self,client_id,client_secret,redirect_uri,scope):
        '''
            Get authentication.
                                            '''
        return SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope)

    def take_control(self,client_id,client_secret,redirect_uri,scope):
        '''
            Grant control.
                Attributes must be correct and valid.
                                                    '''

        return spotipy.Spotify(auth_manager=self.create_spotify_auth(client_id,client_secret,redirect_uri,scope))


    
        