from django.db import models


class Source(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class CastingTime(models.Model):
    name = models.CharField(max_length=100)


class Range(models.Model):
    name = models.CharField(max_length=100)


class Duration(models.Model):
    name = models.CharField(max_length=100)

