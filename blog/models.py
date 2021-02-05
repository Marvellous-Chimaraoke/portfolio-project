from django.db import models
from django.db.models.fields import CharField
from tinymce.models import HTMLField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    body = HTMLField()
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'

    def publish_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')