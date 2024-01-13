from django.db import models
from BlogApp.models import Post

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)