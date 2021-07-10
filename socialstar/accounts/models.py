from django.contrib.auth.models import User as auUser, PermissionsMixin
from django.db import models


# Create your models here.
class User(auUser, PermissionsMixin):
    def __str__(self):
        return self.username
