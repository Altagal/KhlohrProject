import json


def get_card_from_slug(card_slug):
    with open("core/artifact/deck/index.json", 'r') as f:
        index_data = json.load(f)

    for index_obj in index_data:
        if index_obj["slug"] == card_slug:
            with open("core/artifact/deck/" + index_obj["type"] + ".json", 'r') as f:
                deck_data = json.load(f)

            for card_obj in deck_data:
                if card_obj["slug"] == card_slug:
                    card = card_obj
                    break
            break
        else:
            # Return Not Found card.
            card = {
                "slug": "err",
                "name": "Card Not Found",
                "type": "error",
                "type_full": "Error",
                "desc": "",
                "source": "Stone Mirror"
            }

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
