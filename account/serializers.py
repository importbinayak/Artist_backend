from rest_framework import serializers
from .models import User,FriendshipRequest
# from post.serializers import Use

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','friends_count']
        
        
class FriendshipSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    class Meta:
        model=FriendshipRequest
        fields=['id','created_by']