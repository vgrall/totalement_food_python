from django.shortcuts import render  # render permet d'aller chercher un template
from django.http import HttpResponse
from .models import Recette


def index(request):
    listerecettes = Recette.objects.all()

    return render(request, 'totalement_food/index.html', {'listerecettes': listerecettes})


def get_recette(request, recette_id):
    recette = Recette.objects.get(id=recette_id)
    print(recette)
    return render(request, 'totalement_food/recette.html', {'recette': recette})

# ajouter une vue pour la liste des produits

