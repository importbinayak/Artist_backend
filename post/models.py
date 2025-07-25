from django.db import models
import uuid
from account.models import User


# Create your models here.

class PostAttachment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image=models.ImageField(upload_to='post_attachments')
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    body=models.TimeField(blank=True,null=True)
    
    attachments=models.ManyToManyField(PostAttachment,blank=True,null=True)
    
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)