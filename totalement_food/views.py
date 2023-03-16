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


# créer une vue pour totalement_food/les_categories.html

def les_categories(request):
    listecategories = Categorie.objects.all()

    return render(request, 'totalement_food/les_categories.html', {'listecategories': listecategories})


# créer une vue pour totalement_food/la_categorie.html


def get_categorie(request, categorie_id):
    categorie = Categorie.objects.get(id=categorie_id)

    return render(request, 'totalement_food/la_categorie.html', {'categorie': categorie})
