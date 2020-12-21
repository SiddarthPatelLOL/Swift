from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

from dotenv import load_dotenv
from src import auth
import os

load_dotenv()

@xframe_options_exempt # Allows iframes on the host chrome extension  
def index(request):

    return HttpResponse("Initial Test")