from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt # Allows iframes on the host extension  
def index(request):

    return HttpResponse("Initial Test")