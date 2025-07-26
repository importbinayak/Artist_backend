from django.urls import path
from .api import post_list,post_create


urlpatterns = [
    path('',post_list,name='post'),
    path('create/',post_create,name='post_create'),
]
