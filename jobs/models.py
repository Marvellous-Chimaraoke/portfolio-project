from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, default=0)
    summary = models.CharField(max_length=400)
    URL = models.URLField(max_length=200, default=0)
    
    def __str__(self):
        return self.title
