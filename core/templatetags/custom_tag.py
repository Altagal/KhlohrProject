import math

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def ability_modifier(value):
    try:
        value = int(value)
    except:
        return ''

    modifier = math.floor((value - 10) / 2)
    if modifier > -1:
        modifier = "+" + str(modifier)

    return str(value) + " (" + str(modifier) + ")"
