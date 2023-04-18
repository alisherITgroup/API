from django.db import models
from django.contrib.auth.models import User
from random import choice
from datetime import datetime

def slugify():
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    date = str(datetime.now()).replace(" ", "")
    date = date.replace(":", "")
    date = date.replace(".", "")
    date = date.replace("-", "")
    slug = ""
    for i in range(5):
        slug += choice(uppers)
        slug += choice(lowers)
        slug += choice(digits)
        slug += choice(date) 
    return slug.replace(slug[0], "p")

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Maqola muallifi")
    slug = models.CharField(max_length=30, default=slugify, editable=False, unique=True, verbose_name="Maqola slugi")
    title = models.CharField(max_length=200, verbose_name="Maqola sarlavhasi")
    body = models.TextField(verbose_name="Maqola matni")
    tags = models.ManyToManyField(Tag, related_name="post_tags")
    likes = models.ManyToManyField(User, related_name="post_likes")
    unlikes = models.ManyToManyField(User, related_name="post_unlikes")
    viewers = models.ManyToManyField(User, related_name="post_viewers")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def count(self):
        return Post.objects.all().count()
    
    def count_likes(self):
        return self.likes.count()
    
    def count_unlikes(self):
        return self.unlikes.count()
    
    def count_viewers(self):
        return self.viewers.count()
    

class Comment(models.Model):
    reply_id = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_comment_author")
    body = models.TextField(verbose_name="Maqola izoh tanasi")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

