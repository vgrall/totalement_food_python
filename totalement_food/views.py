from django.shortcuts import render  # render permet d'aller chercher un template
from django.http import HttpResponse
from .models import Recette

from .models import Categorie


def index(request):
    listerecettes = Recette.objects.all()

    return render(request, 'totalement_food/index.html', {'listerecettes': listerecettes})


def get_recette(request, recette_id):
    recette = Recette.objects.get(id=recette_id)

    return render(request, 'totalement_food/recette.html', {'recette': recette})


def liste_categories(request):
    categories_liste = Categorie.objects.all()
    return render(request, 'totalement_food/liste_categorie.html', {'categories_liste': categories_liste})


def vue_categorie(request, categorie_id):
    categorie = Categorie.objects.get(id=categorie_id)
    print('hello')

    return render(request, 'totalement_food/vue_categorie.html', {'categorie': categorie})
