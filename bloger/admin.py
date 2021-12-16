from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id','status','slug','author','user')
    prepopulated_fields = {'slug':('title',),}
admin.site.register(models.Category)



@admin.register(models.CommentBlog)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',  'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')