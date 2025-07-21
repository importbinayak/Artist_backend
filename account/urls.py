from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from account.api import *


urlpatterns = [
    path('login/',TokenObtainPairView,name="token_obtain"),
    path('refresh',TokenRefreshView,name='token_refresh'),
    
    
    path('signup',signup,name="signup")
    
]
