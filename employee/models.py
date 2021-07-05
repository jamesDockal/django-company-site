from django.db import models
from django.db.models.expressions import F

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='about_images', blank=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField(blank=False)
    text = models.TextField(blank=False)

    def __str__(self):
        return self.email
