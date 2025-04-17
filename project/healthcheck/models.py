from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


def __str__(self):
    return self.name