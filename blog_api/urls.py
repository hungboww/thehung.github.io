from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, PostListDetailfilter,CreatePost,AdminPostDetail,EditPost,DetelePost,CommentDetail

app_name = 'blog_api'

urlpatterns = [
   path('posts/', PostDetail.as_view(), name='detailcreate'),
   path('', PostList.as_view(), name='listcreate'),
   path('comment/<int:pk>',CommentDetail.as_view(), name='comment'),
   path('search/', PostListDetailfilter.as_view(), name='postsearch'),
   path('admin/create/',CreatePost.as_view(), name='createpost'),
   path('admin/edit/postdetail/<int:pk>', AdminPostDetail.as_view(), name='admindetailpost'),
   path('admin/edit/<int:pk>', EditPost.as_view(),name='editpost'),
   path('admin/detele/<int:pk>', DetelePost.as_view(),name='deletepost'),
]


