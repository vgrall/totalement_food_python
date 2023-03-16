
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('recettes/<int:recette_id>', views.get_recette, name="la_recette"),
    path('les_categories', views.les_categories, name="liste_categorie"),
    # path('la_categorie/<int:categorie_id>',
    #      views.get_categorie, name="la_categorie"),


]
