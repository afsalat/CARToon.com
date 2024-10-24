from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class customUser(AbstractUser):
    contact_number = models.CharField(max_length=100)
    place = models.TextField()
    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True, help_text='The groups this user belongs to.', verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')

    def __str__(self):
        return self.username