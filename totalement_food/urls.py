
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('recettes/<int:recette_id>', views.get_recette, name="la_recette"),

    path('categories', views.liste_categories, name="liste_categories"),

    path('categories/<int:categorie_id>',
         views.vue_categorie, name="vue_categorie"),

    path('ingredients', views.liste_ingredients, name='liste_ingredients'),

    path('ingredients/<int:ingredient_id>',
         views.vue_ingredient, name='vue_ingredient'),

    path('configuration', views.configuration,
         name="liste_configuration"),


]
