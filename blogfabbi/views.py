from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# from commont.pagination import CustomPagination
from commont.pagination import CustomPagination
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    # pagination_class = [CustomPagination]

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field  = 'slug'
    permission_classes = [IsAuthenticated]

class BlogPostFeaturedView(ListAPIView):

    queryset = BlogPost.objects.all().filter(featured = True)
    serializer_class = BlogPostSerializer
    loockup_field = 'slug'
    permission_classes = [IsAuthenticated]


