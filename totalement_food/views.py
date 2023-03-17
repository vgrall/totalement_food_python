from django.shortcuts import render  # render permet d'aller chercher un template
from django.http import HttpResponse
from .models import Recette
from .models import Lexique


def index(request):
    listerecettes = Recette.objects.all()

    return render(request, 'totalement_food/index.html', {'listerecettes': listerecettes})


def get_recette(request, recette_id):
    recette = Recette.objects.get(id=recette_id)

    return render(request, 'totalement_food/recette.html', {'recette': recette})


# créer une vue pour totalement_food/les_categories.html

def les_categories(request):

    return render(request, 'totalement_food/les_categories.html')


def lexique(request):

    return render(request, 'totalement_food/lexique.html')
