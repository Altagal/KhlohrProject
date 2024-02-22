import datetime
import random

from django.shortcuts import render
from cardmaker.util import get_card_from_slug, get_deck, get_daily_card, get_randon_card
from core import settings


def home(request):
    context = {
        # "card": get_daily_card(),
        "card": get_randon_card(),
    }

    return render(request, 'cardviewer/home.html', context)


def card_view(request, card_slug):
    card = get_card_from_slug(card_slug)

    # IF MAGIC SCHOOL
    if card["type"]["slug"] == "magic_school":
        magic_school_spell_list = []
        for spell_card in get_deck("spell"):
            # Se spell.magic_scholl é igual a magic_school slug
            if spell_card["magic_school"]["slug"] == card["slug"]:
                magic_school_spell_list.append(spell_card)
        context = {
            'card': card,
            'range': range(10),
            'table_list': magic_school_spell_list,
        }

    # IF CLASS
    elif card["type"]["slug"] == "class":
        context = {
            'card': card,
            'level_range': range(1, 21),
            'class_feature_list': get_deck("class_feature"),
        }

    # IF SUBCLASS
    elif card["type"]["slug"] == "subclass":
        context = {
            'card': card,
            'subclass_feature_list': get_deck("subclass_feature")
        }
    else:
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


def item_list(request):
    context = {
        "plural_type_name": "Itens",
        "rarity_list": ["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact", "Other"],
        "table_list": get_deck("item"),
    }

    return render(request, 'cardviewer/item_table_view.html', context)


def infusion_list(request):
    context = {
        "plural_type_name": "Infusions",
        "table_list": get_deck("infusion"),
    }

    return render(request, 'cardviewer/infuse_table_view.html', context)


def ability_score_skill_list(request):
    context = {
        "plural_type_name": "Ability Scores and Skills",
        "ability_score_list": get_deck("ability_score"),
        "skill_list": get_deck("skill"),
    }

    return render(request, 'cardviewer/ability_score_skill_table_view.html', context)


def feat_list(request):
    context = {
        "plural_type_name": "Feats",
        "table_list": get_deck("feat"),
    }

    return render(request, 'cardviewer/feat_table_view.html', context)


def class_subclass_list(request):
    context = {
        "plural_type_name": "Classes and Subclasses",
        "class_list": get_deck("class"),
    }

    return render(request, 'cardviewer/class_subclass_table_view.html', context)


def metamagic_list(request):
    context = {
        "plural_type_name": "Metamagics",
        "table_list": get_deck("metamagic"),
    }

    return render(request, 'cardviewer/table_view.html', context)


def eldritch_invocation_list(request):
    context = {
        "plural_type_name": "Eldritch Iinvocations",
        "table_list": get_deck("eldritch_invocation"),
    }

    return render(request, 'cardviewer/eldritch_invocation_table_view.html', context)


def battle_maneuver_list(request):
    context = {
        "plural_type_name": "Battle Maneuvers",
        "table_list": get_deck("battle_maneuver"),
    }

    return render(request, 'cardviewer/table_view.html', context)


def fighting_style_list(request):
    context = {
        "plural_type_name": "Fighting Styles",
        "table_list": get_deck("fighting_style"),
    }

    return render(request, 'cardviewer/table_view.html', context)