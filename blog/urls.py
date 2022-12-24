from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserListView, \
    LatestPostListView
from .api import PostAPIView, PostAPIDetailView, CommentAPICreateView
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework import routers
# from .api import PostViewSet

from django.views.generic.dates import ArchiveIndexView
from .models import Post


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('latest-posts/', LatestPostListView.as_view(), name='latest'),


    path('user/<str:username>', UserListView.as_view(), name='user-posts'),
    path('api/', PostAPIView.as_view()),
    path('api/<int:pk>/', PostAPIDetailView.as_view()),
    path('comment/', CommentAPICreateView.as_view()),



]

