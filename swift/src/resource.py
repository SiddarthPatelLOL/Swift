import requests, os

def getStream(username):
    """
    Gets information about active streams. Streams are returned sorted by
    number of current viewers, in descending order. Across multiple pages
    of results, there may be duplicate or missing streams, as viewers join
    and leave streams.

    The response has a JSON payload with a data field containing an array
    of stream information elements and a pagination field containing
    information required to query for more streams.

    ref: https://dev.twitch.tv/docs/api/reference#get-streams
    """
    URL = "https://api.twitch.tv/helix/streams"

    accessToken = os.getenv('ACCESS_TOKEN') 
    clientId = os.getenv('CLIENT_ID')
    headers = {
        'Authorization': f'Bearer {str(accessToken)}',
        'Client-Id': str(clientId)
    }

    params = {
        'user_login': username,
    }

    response = requests.get(URL, headers=headers, params=params)
    response = response.json()

    try:
        response = response['data'][0]
    except KeyError:
        return False
    except IndexError:
        return False
    
    viewerCount = response['viewer_count']
    viewerCount = '{:,}'.format(viewerCount)
    response['viewer_count'] = viewerCount 

    return response
    


def profile(username):
    """
    Gets information about one or more specified Twitch users. Users are 
    identified by optional user IDs and/or login name.

    The response has a JSON payload with a data field containing an array 
    of user-information elements.

    ref: https://dev.twitch.tv/docs/api/reference#get-users
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

    try:
        response = response['data'][0]
    except KeyError:
        return False
    except IndexError:
        return False

    broadcasterType = response['broadcaster_type']
    accountCreated = response['created_at']
    totalViewCount = response['view_count']

    totalViewCount = int(totalViewCount)
    totalViewCount = '{:,}'.format(totalViewCount)
    
    response['view_count'] = totalViewCount
    response['created_at'] = accountCreated[0:10] 
    if broadcasterType == "":
        response['broadcaster_type'] = "Regular User"

    return response