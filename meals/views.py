from django.shortcuts import render
from django.http import HttpResponse
# Сразу откроем index: 
def index(request):
    return render(request, 'meals/index.html')

