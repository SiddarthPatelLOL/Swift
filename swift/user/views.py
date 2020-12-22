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

    return render(request, 'user/index.html')

@xframe_options_exempt # Allows iframes on the host chrome extension  
@csrf_exempt
@auth.checker
def query(request):

    if request.method == "POST":
        username = request.POST['search']
    
    response = resource.profile(username)
    response = response['data'][0]

    context = {'response': response}
    return render(request, 'user/query.html', context)
    