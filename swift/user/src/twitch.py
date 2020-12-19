import requests, os


def getAccessToken(client_id, client_secret, grant_type):
    """
    Requests app access token via Twitch API and returns a JSON format 
    converted to a dictionary when returned to callee in another file. 
    """

    URL = "https://id.twitch.tv/oauth2/token"

    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type,  
    }

    response = requests.post(URL, params=params)
    response = response.json()
    
    return response
