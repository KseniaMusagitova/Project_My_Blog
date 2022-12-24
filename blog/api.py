from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, generics
from .serializers import PostSerializer, PostDetailSerializer, CommentCreateSerializer

from .models import Post, Comment

class PostAPIView(APIView):
    """Вывод списка постов:"""
    def get(self, request):
        posts = Post.objects
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostAPIDetailView(APIView):
    """Вывод поста:"""
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class CommentAPICreateView(APIView):
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)