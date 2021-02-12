from django.db import models
from django.utils import timezone


# Create your models here.

class yazi(models.Model):
    creater = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    text = models.TextField()
    image =  models.ImageField(upload_to='static/image', default = None, null = True, blank = True)
    created_date = models.DateTimeField( default=timezone.now )
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

