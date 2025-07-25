from django.urls import path
from .api import post_list


urlpatterns = [
    path('',post_list,name='post'),
]
