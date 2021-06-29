from django.db import models
from django.conf import settings
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50,null=False)
    body = models.TextField(max_length=500, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True, max_length=70)
