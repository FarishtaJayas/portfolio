from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    description = models.TextField()