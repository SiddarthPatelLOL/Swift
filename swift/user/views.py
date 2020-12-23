from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt


from dotenv import load_dotenv
from src import auth, resource


load_dotenv()


@xframe_options_exempt # Allows iframes on the host chrome extension  
@auth.checker
def index(request):
    """
    Renders a search box for the user to query information about a
    specific user on twitch.
    """

    return render(request, 'user/index.html')

@xframe_options_exempt # Allows iframes on the host chrome extension  
@csrf_exempt
@auth.checker
def query(request):
    """
    Accepts twitch username entered by the user making the query and
    renders template containing the information of the twitch user.
    """

    username = ""
    if request.method == "POST":
        username = request.POST['search']
    
    profileInfo = resource.profile(username)
    streamInfo = resource.getStream(username)

    if not profileInfo:
        context = {'error': True}
        return render(request, 'user/index.html', context)
    else:
        context = {'profile': profileInfo, 'stream': streamInfo}
        return render(request, 'user/query.html', context)
    