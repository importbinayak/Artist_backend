from django.db import models
import uuid
from account.models import User
from django.utils import timezone
from django.utils.timesince import timesince


# Create your models here.
class Likes(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_by=models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


class PostAttachment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image=models.ImageField(upload_to='post_attachments')
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    body=models.TextField(blank=True,null=True)
    
    attachments=models.ManyToManyField(PostAttachment,blank=True,null=True)
    
    likes=models.ManyToManyField(Likes,blank=True)
    likes_count=models.IntegerField(default=0)
    
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=("-created_at",)
    
    @property
    def created_at_min(self):
        if self.created_at:
            return timesince(self.created_at,timezone.now()) + " ago"
        return "Just now"