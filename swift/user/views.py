from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

from dotenv import load_dotenv
from src import auth


load_dotenv()


@xframe_options_exempt # Allows iframes on the host chrome extension  
@auth.checker
def index(request):

    return HttpResponse("Initial Test")