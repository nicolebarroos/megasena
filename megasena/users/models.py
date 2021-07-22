from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    email = models.CharField('Email', max_length=50)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username
