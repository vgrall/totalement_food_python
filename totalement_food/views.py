from django.shortcuts import render  # render permet d'aller chercher un template
from django.http import HttpResponse
from .models import Recette
from .models import Ingredients


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

    return render(request, 'totalement_food/vue_categorie.html', {'categorie': categorie})


def liste_ingredients(request):
    ingredients_liste = Ingredients.objects.all()

    return render(request, 'totalement_food/liste_ingredients.html', {'ingredients_liste': ingredients_liste})


def vue_ingredient(request, ingredient_id):
    ingredient = Ingredients.objects.get(id=ingredient_id)

    return render(request, 'totalement_food/vue_ingredient.html', {'ingredient': ingredient})


def configuration(request):
    ingredients_liste = Ingredients.objects.all()
    categorie_liste = Categorie.objects.all()
    print(ingredients_liste)
    print(categorie_liste)
    return render(request, 'totalement_food/liste_configuration.html', {'categorie_liste': categorie_liste, 'ingredients_liste': ingredients_liste})




# def liste_configuration(request):
#     configuration_liste = Configuration.objects.all()
#     print('helloooo')
#     return render(request, 'totalement_food/liste_configuration.html', {'configuration_liste': configuration_liste})
