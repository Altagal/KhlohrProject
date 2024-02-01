import json

from django.shortcuts import render
from cardmaker.util import get_card_from_slug, get_deck


def home(request):
    context = {
    }

    return render(request, 'cardviewer/home.html', context)


def card_view(request, card_slug):
    card = get_card_from_slug(card_slug)

    if card["type"]["slug"] == "magic_school":
        magic_school_spell_list = []
        for spell_card in get_deck("spell"):
            # Se spell.magic_scholl é igual a magic_school slug
            if spell_card["magic_school"]["slug"] == card["slug"]:
                magic_school_spell_list.append(spell_card)

        context = {
            'card': card,
            "range": range(10),
            'table_list': magic_school_spell_list,

        }
        return render(request, 'cardviewer/card_view.html', context)
    context = {
        'card': card,
    }
    return render(request, 'cardviewer/card_view.html', context)


def condition_list(request):
    context = {
        "plural_type_name": "Conditions",
        "table_list": get_deck("condition"),
    }

    return render(request, 'cardviewer/table_view.html', context)


def spell_list(request):
    context = {
        "plural_type_name": "Spells",
        "range": range(10),
        "table_list": get_deck("spell"),
    }

    return render(request, 'cardviewer/spell_table_view.html', context)
