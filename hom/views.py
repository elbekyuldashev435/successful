from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return HttpResponse("<h1>Welcome!<h1>\n<h2>This website has been created recently.<h2>")


def news(request):
    return HttpResponse("<h1>Foreign Secretary meeting with Foreign Minister of Mongolia, April 2024<h1>")