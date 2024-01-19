from cardmaker.models import MagicSchool


def sidebar_context(request):
    context = {
        "magic_school_list_context_processors": MagicSchool.objects.all(),
    }
    return context
