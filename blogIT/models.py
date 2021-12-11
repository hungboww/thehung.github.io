from django.db import models
from django.conf import settings

# Create your models here.
class BlogTags(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    tag = models.ManyToManyField(BlogTags, related_name="blog_tag")
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='blog_post')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def meta(self):
        ordering = ("-created_at")

class BlogComments(models.Model):
    blog = models.ForeignKey(Blog, related_name="blog_comment")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='blog_comment')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def meta(self):
        ordering = ("-created_at")