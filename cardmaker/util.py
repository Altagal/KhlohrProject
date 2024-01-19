import json

from django.apps import apps

from cardmaker.models import Other


def get_card_from_slug(card_slug):
    for card_type in apps.get_models():
        if hasattr(card_type, "slug"):
            try:
                return card_type.objects.get(slug=card_slug)
            except:
                pass

    card = Other.objects.get(slug="err")
    card.set_error_face(card_slug)
    return card


def get_card(slug_list):
    card_list = []
    for slug in slug_list:
        card = get_card_from_slug(slug)
        card_list.append(card)
    return card_list


def get_deck(deck_name):
    f = open("core/artifact/deck/" + deck_name + ".json")
    data = json.load(f)
    return data
