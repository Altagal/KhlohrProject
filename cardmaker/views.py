from django.http import HttpResponse
from django.shortcuts import render, redirect

from cardmaker.util import get_card, get_card_from_slug


def cart_view(request):
    # if 'stored_cards' not in request.session:
    #     request.session['stored_cards'] = []

    context = {
        "card_list": get_card(request.session['stored_cards'])
    }

    return render(request, 'cardviewer/cart_view.html', context)


def card_print(request):
    lista_auxiliar = [
        # lista de cartas upadas de modo artificial para teste
    ]

    card_list = []

    for slug in lista_auxiliar:
        card = get_card_from_slug(slug)
        card_list.append(card)

    for slug in request.session['stored_cards']:
        card = get_card_from_slug(slug)
        card_list.append(card)

    context = {
        "card_list": card_list

    }

    return render(request, 'cardmaker/print_cards.html', context)


# mudar pra posição ao inves de slug
def remove_stored_card(request, card_slug):
    if card_slug in request.session['stored_cards']:
        request.session['stored_cards'].remove(card_slug)
        request.session.modified = True
    else:
        print("Erro remove item from cart. " + card_slug + " not found.")

    return redirect('cart_view')


def remove_all_stored_card(request):
    request.session['stored_cards'].clear()
    request.session.modified = True

    return redirect('cart_view')


def store_card_in_cart(request, card_slug):
    if 'stored_cards' in request.session:
        request.session['stored_cards'].append(card_slug)
    else:
        request.session['stored_cards'] = [card_slug]

    request.session.modified = True
    return HttpResponse()
