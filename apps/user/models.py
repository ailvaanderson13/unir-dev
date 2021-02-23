from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    celular = models.CharField(max_length=11, blank=True, null=True)
    reset_password = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'