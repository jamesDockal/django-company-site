from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='about_images', blank=False)

    def __str__(self):
        return self.title
