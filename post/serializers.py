from rest_framework import serializers
from .models import Post,PostAttachment
from account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    created_at_min=serializers.ReadOnlyField()
    class Meta:
        model=Post
        fields=['id','body','created_by','created_at','created_at_min']