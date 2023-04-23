import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from social_media_api import settings


def user_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)

    filename = f"{slugify(instance.id)}-{uuid.uuid4()}.{extension}"

    return os.path.join("uploads/users/", filename)


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to=user_image_file_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following_users", symmetrical=False, blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers_users", symmetrical=False, blank=True)

    def __str__(self):
        return self.username
