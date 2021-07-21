from django.db import models
from django.utils.timezone import now
from users.models import Users


class Plays(models.Model):
    dozens = models.CharField('Name', max_length=50)
    creation_date = models.DateField('Data da jogada', default=now)
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        null=True
    )
    class Meta:
        verbose_name = 'Jogada'
        verbose_name_plural = 'Jogadas'


    def __str__(self):
        return self.dozens


    objects = models.Manager()
