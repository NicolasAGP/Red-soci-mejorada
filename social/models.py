from django.contrib import auth
from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone

from django.contrib.auth import BACKEND_SESSION_KEY, get_user_model
User = get_user_model()

def user_directory_path(instance, filename):
    return 'users/socialposts/{0}'.format(filename)

def dm_directory_path(instance, filename):
    return 'user/messages/{0}'.format(filename)

class SocialPost(models.Model):
    body=models.TextField()
    image = models.ManyToManyField('Image', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_post_author')
    likes = models.ManyToManyField(User, blank=True, related_name='Likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

class SocialComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_comment_author')
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')

class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
