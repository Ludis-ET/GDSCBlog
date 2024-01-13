from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255,unique=True)
    content = models.TextField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Post/')
    tags = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.title