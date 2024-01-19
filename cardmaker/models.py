from django.db import models
from cardsetting.models import Source


class CardAbstract(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    desc = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class MagicSchool(CardAbstract):
    pass


class Condition(CardAbstract):
    pass


class Miscellanea(CardAbstract):
    alt_name = models.CharField(max_length=100)


class Other(CardAbstract):
    alt_name = models.CharField(max_length=100)
