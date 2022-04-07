from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return HttpResponse("<h1>Welcome to the project first<h1>")
def second(request):
    return HttpResponse("<h1>Welcome to the project second<h1>")

# Create your views here.
