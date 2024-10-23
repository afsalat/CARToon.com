from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUser(AbstractUser):
    contact_number = models.CharField(max_length=100)
    place = models.TextField()

    def __str__(self):
        return self.username