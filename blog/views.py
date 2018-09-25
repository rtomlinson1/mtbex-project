from django.shortcuts import render
from django.http import HttpResponse
from .models import blog, rating, review, blogposts
# Create your views here.
def index(request):
    blogs = blog.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', {'blogs':blogs})

def rating(request):
    return render(request, 'blog/ratings.html')

def review(request):
    return render(request, 'blog/reviews.html')

def blogpost(request):
    return render(request, 'blog/blogposts.html')

    #return HttpResponse("Index Page")
    