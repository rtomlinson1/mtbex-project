from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vidsindex(request):
    return HttpResponse("Videos Index Page")