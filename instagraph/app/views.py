from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    BASE_URL = "https://api.instagram.com/oauth/authorize/?"
    REDIRECT_URI = "http://127.0.0.1:5000/grant-access"
    url = BASE_URL + "client_id={}&redirect_uri={}&response_type=code".format(CLIENT_ID, REDIRECT_URI)
    return HttpResponseRedirect(url)
    #return render(request, "index.html")