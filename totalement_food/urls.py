
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('recettes/<int:recette_id>', views.get_recette, name="la_recette"),
    path('les_categories', views.les_categories, name="liste_categorie"),
    path('les_categories/lexique',
         views.lexique, name='lexique'),



]
