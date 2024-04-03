import datetime
import json
import random

from django.utils.text import slugify

from core import settings


def get_card_from_slug(card_slug):

    card_slug = slugify(card_slug)

    with open("core/artifact/deck/index.json", 'r') as f:
        index_data = json.load(f)

    #SETUP NOT FOUND CARD
    card = {
        "slug": "err",
        "name": "Card Not Found",
        "type": {
            "slug": "error",
            "name": "Error"
        },
        "desc": "<p>This card may not be indexed yet.</p>",
        "source": "Stone Mirror"
    }

    for index_obj in index_data:
        if index_obj["slug"] == card_slug:
            with open("core/artifact/deck/" + index_obj["type"]["slug"] + ".json", 'r') as f:
                deck_data = json.load(f)

            for card_obj in deck_data:
                if card_obj["slug"] == card_slug:
                    card = card_obj
                    break
            break

    if card["slug"] == "err":
        print(card_slug)
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


def get_daily_card():
    deck = get_deck("index")
    seed = f'{settings.SECRET_KEY}{datetime.date.today()}'
    card_slug = random.Random(seed).choice(deck)
    card = get_card_from_slug(card_slug["slug"])
    return card


def get_randon_card():
    deck = get_deck("index")
    card_slug = random.choice(deck)
    card = get_card_from_slug(card_slug["slug"])
    return card
