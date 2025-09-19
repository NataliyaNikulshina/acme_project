from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, verbose_name="О себе")

    def __str__(self):
        return self.username
