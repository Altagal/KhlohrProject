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
