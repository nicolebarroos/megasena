from django.db import models
from django.utils.timezone import now
from users.models import Users
from django.contrib.postgres.fields import ArrayField

class Plays(models.Model):

    first_dozen = models.CharField('Primeia dezena', blank=False, null=False, max_length=5)
    second_dozen = models.CharField('Segunda dezena', blank=False, null=False, max_length=5)
    third_dozen = models.CharField('Terceira dezena', blank=False, null=False, max_length=5)
    fourth_dozen = models.CharField('Quarta dezena', blank=False, null=False, max_length=5)
    fifth_dozen = models.CharField('Quinta dezena', blank=False, null=False, max_length=5)
    sixth_dozen = models.CharField('Sexta dezena', blank=False, null=False, max_length=5)
    creation_date = models.DateField('Data da jogada', default=now)
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        null=True
    )
    class Meta:
        verbose_name = 'Jogada'
        verbose_name_plural = 'Jogadas'




    objects = models.Manager()
