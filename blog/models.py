from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from datetime import date, timedelta


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_latest(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=7)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments_posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    text = models.TextField(verbose_name='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)


class NewStats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    iphone = models.IntegerField()
    android = models.IntegerField()
    other = models.IntegerField()




