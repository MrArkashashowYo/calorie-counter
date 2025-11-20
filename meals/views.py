from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Это страница раздела Meals.")
# Create your views here.
