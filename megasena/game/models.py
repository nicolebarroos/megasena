from django.db import models


class Plays(models.Model):
    results = models.CharField('Name', max_length=50)

    objects = models.Manager()
