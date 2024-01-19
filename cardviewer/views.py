import json

from django.shortcuts import render
from cardmaker.models import Condition
from cardmaker.util import get_card_from_slug, get_deck


def home(request):
    context = {
    }

    return render(request, 'cardviewer/home.html', context)


def condition_list(request):
    context = {
        "plural_type_name": "Conditions",
        "table_list": Condition.objects.all(),
    }

    return render(request, 'cardviewer/table_view.html', context)

# def condition_list(request):
#
#     context = {
#         "plural_type_name": "Conditions",
#         "table_list": get_deck("Conditions"),
#     }
#
#     return render(request, 'cardviewer/table_view.html', context)


def card_view(request, card_slug):
    obj_card = get_card_from_slug(card_slug)

    # if obj_card.type == "Magic School":
    #     context = {
    #         'obj_card': obj_card,
    #         'cardbase_list': Spell.objects.all().filterby(magic_school=obj_card.id)
    #     }
    #     return render(request, 'cardviewer/table_magic_school_view.html', context)

    context = {
        'obj_card': obj_card,
    }
    return render(request, 'cardviewer/card_view.html', context)
