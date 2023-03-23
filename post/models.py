from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
