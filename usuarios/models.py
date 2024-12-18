from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choice_cargo = (('V', 'Vendedor'),
                    ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choice_cargo)