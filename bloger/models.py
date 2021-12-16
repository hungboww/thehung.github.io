from django.db import models
from django.utils import timezone
from django.conf import settings

from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )
    category = models.ForeignKey(Category, on_delete= models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    user = models.CharField(max_length=22)
    excerpt = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='blog_post')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()
    postobjects = PostObjects()
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)