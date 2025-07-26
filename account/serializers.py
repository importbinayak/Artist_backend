from rest_framework import serializers
from .models import User
# from post.serializers import Use

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email']
        