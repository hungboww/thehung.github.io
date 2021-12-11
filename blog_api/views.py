# from warnings import filters

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
from rest_framework import filters
from bloger.models import Post
from commont.pagination import CustomPagination
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission, SAFE_METHODS, AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.views import APIView
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListAPIView,PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug)
        return Post.objects.filter(slug=slug)

class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=slug']

class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug)
        return Post.objects.filter(slug=slug)

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetelePost(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PostSerializer
    queryset = Post.objects.all()