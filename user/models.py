from django.contrib.auth.models import AbstractUser
from django.db import models

from social_media_api import settings


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following_users", symmetrical=False, blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers_users", symmetrical=False, blank=True)

    def __str__(self):
        return self.username
