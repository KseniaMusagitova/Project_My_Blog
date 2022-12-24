from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    '''Список постов'''

    class Meta:
        model = Post
        fields = ['author', 'title', 'content']


class CommentCreateSerializer(serializers.ModelSerializer):
    '''Добавление комментария к посту'''

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    '''Вывод комментария отзывы'''

    class Meta:
        model = Comment
        exclude = []


class PostDetailSerializer(serializers.ModelSerializer):
    '''Пост'''
    comments_posts = CommentSerializer(many=True)

    class Meta:
        model = Post
        exclude = []



