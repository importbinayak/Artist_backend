from rest_framework import serializers
from .models import Post,PostAttachment,Comment
from account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    created_at_min=serializers.ReadOnlyField()
    class Meta:
        model=Post
        fields=['id','body','likes_count','comment_count','created_by','created_at','created_at_min']

class CommentSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields=["id","body","created_at","created_by"]
        
class PostDetail(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    created_at_min=serializers.ReadOnlyField()
    comments=CommentSerializer(read_only=True)
    class Meta:
        model=Post
        fields=['id','body','likes_count','comments','created_by','created_at','created_at_min']