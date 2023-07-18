from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class YourQUser(AbstractUser):

    def __str__(self) -> str:
        return f"{self.username}"