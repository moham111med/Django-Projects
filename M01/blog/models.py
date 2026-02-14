from django.db import models
#we add it
from django.utils import timezone 
from django.contrib.auth.models import User 

# Create your models here.
#we add it 
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'
    #Definig a default sort order
    class Meta:
        ordering=['-publish']
    #Adding a status field
        indexes=[
            models.Index(fields=['-publish']),
        ]
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    #Adding datetime fields
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    #adding many-to-one relationship
    author=models.ForeignKey(User,blank=True,on_delete=models.CASCADE,related_name='blog_posts')

    #to make message readable in Dashboard admin
    def __str__(self):
        return self.title 
       #return self.body[0:10] 
#==============================================
'''
     Model                               DB Table
-------------------             --------------------------
Post                            blog_post
-------------------             --------------------------
id   -> BigAutoField|            id    -> integer PrimaryKey
title-> CharField   |            title -> varchr(250)
slug -> SlugField   | <--------> slug  -> varchr(250)
body -> ForeignKey  |            body  -> text
'''
#python manage.py shell
#user=User.objects.get(username='m')
#post=Post(title='Another',slug='another-post',body='anything',author=user)
#post.save() to update or save or refresh
#post=Post.objects.filter(publish__year=2022)
#post=Post.objects.get(id=1)