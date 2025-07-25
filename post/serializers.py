from rest_framework import serializers
from .models import Post,PostAttachment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        models=Post
        fields=['id','body','created_by','created_at']