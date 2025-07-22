from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from account.api import *


urlpatterns = [
    #JWT token
    path('login/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    
    
    path('signup/',signup,name="signup"),
    path('me/',me,name="me")
    
]
