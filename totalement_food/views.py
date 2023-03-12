from django.shortcuts import render  # render permet d'aller chercher un template
from django.http import HttpResponse


def index(request):

    return render(request, 'totalement_food/index.html')


def la_recette(request):

    return render(request, 'totalement_food/recette.html')
