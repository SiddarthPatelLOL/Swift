import requests, os, time


def storeRequestedAccessToken():
    """
    Function does two things:

    *   Requests app access token via Twitch API and returns a python dictionary
        containing the API response.
    
    *   Then stores the response containing the app access token and the expiry
        date converted to time since epoch in an .env file as environment
        variable stored relative to the caller directory. 

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

    # Stores the token and expiry date (in seconds since epoch) in env vars 
    os.system(f"echo 'ACCESS_TOKEN=\"{response['access_token']}\"' >> .env")
    os.system(f"echo 'EXPIRES_IN={response['expires_in']}' >> .env")


def checker(view):
    """
    Checks the existence of app access token in the environment variable. If
    not, requests and stores the same.

    If it does exist, there is another check to ensure the validity of the app
    access token. If it is expired, it removes it and requests a new app access
    token and stores the same. 

    """
    # Check to ensure app access token exists in the environment variable.
    if not os.getenv('ACCESS_TOKEN'):
        
        storeRequestedAccessToken()
        
    # Check to ensure the validity of the app access token.
    expiresIn = os.getenv('EXPIRES_IN')
    realTime = time.time()

    # Checks if remaining time is below the set custom threshhold.
    remainingSecondsInEpoch = float(expiresIn) - realTime 
    customThreshhold = 3600

    if remainingSecondsInEpoch <= customThreshhold:            

        # Removes last line in .env file.
        os.system("sed -i '$d' .env")
        os.system("sed -i '$d' .env") 
        
        storeRequestedAccessToken()
    else:
        # App access token has not expired, view is allowed to be called.
        
        def wrapper(*args, **kwargs):
            return view(*args, **kwargs)
        return wrapper
