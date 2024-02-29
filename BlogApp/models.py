# In the "BlogApp" app, extend the "Post" model with the following fields and constraints:
# Title (CharField, unique=True)
# Content (TextField)
# Category (CharField)
# Image (ImageField)
# Tags (ArrayField(CharField))

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/')
    tags = models.ArrayField(models.CharField(max_length=100), blank=True)
