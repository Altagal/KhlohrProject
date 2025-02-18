from cardmaker.util import get_deck


def layout_context(request):
    if 'stored_cards' not in request.session:
        request.session['stored_cards'] = []

    cards_in_cart = 0
    if request.session['stored_cards']:
        cards_in_cart = len(request.session['stored_cards'])



    context = {
        "magic_school_list_context_processors": get_deck("magic_school"),
        "index_list_context_processors": get_deck("index"),
        "cards_in_cart": cards_in_cart
    }
    return context

