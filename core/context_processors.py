from cardmaker.util import get_deck


def sidebar_context(request):
    context = {
        "magic_school_list_context_processors": get_deck("magic_school"),
        "conditon_list_context_processors": get_deck("condition")
    }
    return context
