from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    has_2fa = models.BooleanField(default=False)