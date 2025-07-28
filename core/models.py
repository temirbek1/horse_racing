from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass  # можно добавить поля позже

class Horse(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.breed})'
