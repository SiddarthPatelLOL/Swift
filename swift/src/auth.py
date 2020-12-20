from os.path import dirname
from dotenv import main
import requests, os, time


def getAccessToken():
    """
    Requests app access token via Twitch API and returns a python dictionary
    containing the API response. 
    """
    URL = "https://id.twitch.tv/oauth2/token"

    params = {
        'client_id': os.getenv("CLIENT_ID"),
        'client_secret': os.getenv("CLIENT_SECRET"),
        'grant_type': "client_credentials",  
    }

    response = requests.post(URL, params=params)
    response = response.json()

    # Convert value (in seconds) of the key 'expires_in' to unix epoch. 
    response['expires_in'] = float(response['expires_in']) + time.time()

    return response

def storeAccessToken(accessToken, expiresIn):
    """
    Stores the app access token and it's expiry date since epoch in an .env
    file as environment variable stored relative to the caller directory. 
    """
    os.system(f"echo 'ACCESS_TOKEN=\"{accessToken}\"' >> .env")
    os.system(f"echo 'EXPIRES_IN={expiresIn}' >> .env")
    