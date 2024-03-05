from django.db import models


class Positions(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()


class Workers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    position = models.ForeignKey(Positions, blank=True, null=True, on_delete=models.CASCADE)
