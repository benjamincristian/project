from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
    # small_description is a little insight of the actual content. This is going to be showed
    small_description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog', blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def total_like(self):
        return self.likes.count()

    def total_dislike(self):
        return self.dislikes.count()


class Comment(models.Model):
    post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.post_id.title, self.name)


