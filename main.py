import time
import os

from app_client import *
from spotify import Spotify

sp = Spotify().take_control(
             client_id=CLIENT_ID,
             client_secret=CLIENT_SECRET,
             redirect_uri=REDIRECT_URI,
             scope=SCOPE)

'''

    1)IF song is playing -> do nothing

    2)IF song is not playing -> sleep for 15 mins
        then check again if song is still idle

            2.1)IF idle -> shutdown
            2.2)else -> restart the loop

                                                '''
while True:
    try:
        if not sp.currently_playing()['is_playing']  : 
            print('interrupt')
            time.sleep(15*60)
            if sp.currently_playing() == None  : os.system("shutdown /s /t 1")
            else : pass
        else : print("working")
    except:

        if sp.currently_playing() == None  : 
            print('interrupt')
            time.sleep(15*60)
            if sp.currently_playing() == None : os.system("shutdown /s /t 1")
            else : pass
        else : print("working")