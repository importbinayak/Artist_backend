from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .forms import PostForm

# Create your views here.

@api_view(['GET'])
def post_list(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return JsonResponse({'data':serializer.data})


@api_view(['POST'])
def post_create(request):
    form=PostForm(request.data)
    if form.is_valid():
        post=form.save(commit=False)
        post.created_by=request.user
        post.save()
        
        serializer=PostSerializer(post)
        return JsonResponse(serializer.data,safe=False)
    else:
        return JsonResponse({'error':'hello says hello'})