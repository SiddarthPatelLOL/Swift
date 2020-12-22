import requests, os


def profile(username):
    """
    """
    URL = "https://api.twitch.tv/helix/users"

    accessToken = os.getenv('ACCESS_TOKEN') 
    clientId = os.getenv('CLIENT_ID')
    headers = {
        'Authorization': f'Bearer {str(accessToken)}',
        'Client-Id': str(clientId)
    }
    
    params = {
        'login': username,
    }

    response = requests.get(URL, headers=headers, params=params)
    response = response.json()

    return response