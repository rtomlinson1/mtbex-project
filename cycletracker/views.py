from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ctindex(request):
    return HttpResponse("Cycle Tracker Index Page")