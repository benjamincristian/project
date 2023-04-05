from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
    small_description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog', blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def total_like(self):
        return self.likes.count()

    def total_dislike(self):
        return self.dislikes.count()

    def total_comments(self):
        return self.comments.count()


class PostComment(models.Model):
    blogpost_connected = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = TextField()
    likes = models.ManyToManyField(User, related_name='comment', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.author) + self.blogpost_connected.title
