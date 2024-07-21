import datetime
import random

from django.shortcuts import render
from cardmaker.util import get_card_from_slug, get_deck, get_daily_card, get_randon_card
from core import settings


def home(request):
    context = {
        "card_daily": get_daily_card(),
        "card_randon": get_randon_card(),
    }

    return render(request, 'cardviewer/home.html', context)


def card_view(request, card_slug):
    card = get_card_from_slug(card_slug)

    # IF MAGIC SCHOOL
    if card["type"]["slug"] == "magic_school":
        context = {
            'card': card,
            "spell_level_range": range(10),
            'table_list': get_deck("spell"),
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
    # IF MONSTER
    elif card["type"]["slug"] == "monster":
        context = {
            'card': card,
            'monster_trait_list': get_deck("monster_trait"),
            'monster_action_list': get_deck("monster_action"),
            'monster_reaction_list': get_deck("monster_reaction"),
            'monster_legendary_action_list': get_deck("monster_legendary_action")
        }
    else:
        context = {
            'card': card,
        }

    return render(request, 'cardviewer/card/include/card_page.html', context)


def condition_list(request):
    context = {
        "plural_type_name": "Conditions",
        "table_list": get_deck("condition"),
    }

    return render(request, 'cardviewer/table/table_generic.html', context)


def spell_list(request):
    context = {
        "spell_level_range": range(10),
        "table_list": get_deck("spell"),
    }

    return render(request, 'cardviewer/table/table_spell.html', context)


def infusion_list(request):
    context = {
        "plural_type_name": "Infusions",
        "table_list": get_deck("infusion"),
    }

    return render(request, 'cardviewer/table/table_requirement.html', context)


def ability_score_skill_list(request):
    context = {
        "ability_score_list": get_deck("ability_score"),
        "skill_list": get_deck("skill"),
    }

    return render(request, 'cardviewer/table/table_ability_score_skill.html', context)


def feat_list(request):
    context = {
        "table_list": get_deck("feat"),
    }

    return render(request, 'cardviewer/table/table_feat.html', context)


def class_subclass_list(request):
    context = {
        "class_list": get_deck("class"),
    }

    return render(request, 'cardviewer/table/table_class_subclass.html', context)


def metamagic_list(request):
    context = {
        "plural_type_name": "Metamagics",
        "table_list": get_deck("metamagic"),
    }

    return render(request, 'cardviewer/table/table_generic.html', context)


def eldritch_invocation_list(request):
    context = {
        "plural_type_name": "Eldritch Invocations",
        "table_list": get_deck("eldritch_invocation"),
    }

    return render(request, 'cardviewer/table/table_requirement.html', context)


def battle_maneuver_list(request):
    context = {
        "plural_type_name": "Battle Maneuvers",
        "table_list": get_deck("battle_maneuver"),
    }

    return render(request, 'cardviewer/table/table_generic.html', context)


def fighting_style_list(request):
    context = {
        "plural_type_name": "Fighting Styles",
        "table_list": get_deck("fighting_style"),
    }

    return render(request, 'cardviewer/table/table_generic.html', context)


def monster_list(request):
    context = {
        "table_list": get_deck("monster"),
        "challenge_rating_range": [0, 1 / 8, 1 / 4, 1 / 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    }

    return render(request, 'cardviewer/table/table_monster.html', context)


def magic_item_list(request):
    context = {
        "rarity_list": ["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact", "Other"],
        "table_list": get_deck("magic_item"),
    }

    return render(request, 'cardviewer/table/table_magic_item.html', context)


def armor_list(request):
    context = {
        "table_list": get_deck("armor"),
    }

    return render(request, 'cardviewer/table/table_armor.html', context)


def weapon_list(request):
    context = {
        "table_list": get_deck("weapon"),
    }

    return render(request, 'cardviewer/table/table_weapon.html', context)


def adventuring_gear_list(request):
    context = {
        "table_list": get_deck("adventuring_gear"),
    }

    return render(request, 'cardviewer/table/table_adventuring_gear.html', context)


def tool_list(request):
    context = {
        "table_list": get_deck("tool"),
    }

    return render(request, 'cardviewer/table/table_tool.html', context)


def conditon_list(request):
    context = {
        "plural_type_name": "Conditions",
        "table_list": get_deck("condition"),
    }

    return render(request, 'cardviewer/table/table_generic.html', context)


def weapon_property_list(request):
    context = {
        "plural_type_name": "Weapon Properties",
        "table_list": get_deck("weapon_property"),
    }

    return render(request, 'cardviewer/table/table_generic.html', context)

