from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from account.api import *


urlpatterns = [
    #JWT token
    path('login/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    
    
    path('signup/',signup,name="signup"),
    path('me/',me,name="me"),
    
    
    path('friends/<uuid:pk>/',friends,name='friends'),
    path('friends/<uuid:pk>/request/',send_friendship_request,name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/',handle_request,name='handle_request')
    
]
