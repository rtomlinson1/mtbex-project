from django.urls import path
from . import views

urlpatterns = [
    path('', views.ctindex, name='ctindex'),
]