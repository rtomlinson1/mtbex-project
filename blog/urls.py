from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogposts/', views.blogposts, name='blogposts'),
    path('ratings/', views.rating, name='ratings'),
    path('reviews/', views.review, name='reviews'),
]