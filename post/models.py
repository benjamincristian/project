from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    likes = models.IntegerField(default=0)
