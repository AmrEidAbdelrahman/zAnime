from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=200)
    arr_date = models.DateTimeField(auto_now_add=True)
    arrieved = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.message}'
