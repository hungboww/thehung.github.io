from datetime import datetime

# import srt as srt
from django.db import models
# from django.conf import settings
# Create your models here.
from datetime import datetime
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User

class Categories(models.TextChoices):
    HTML = 'html'
    PYTHON = 'python'
    REACT = 'react'
    JAVA = 'java'
    JAVASCRIPT = 'javascript'
    C = 'c'
    C1 = 'c++'
    C2 = 'c#'
    RUBY = 'ruby'
    DJANGO = 'django'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50,choices=Categories.choices,default=Categories.HTML)
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    source = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    viewCount = models.IntegerField(default=0)

    def save(self,*args,**kwargs):

        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact = original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-'+str(count)
            count +=1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured = True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        super(BlogPost,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

