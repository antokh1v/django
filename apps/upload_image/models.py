from django.db import models
from .services import count_black_pix
# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


