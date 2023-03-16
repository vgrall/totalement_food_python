
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('recettes/<int:recette_id>', views.get_recette, name="la_recette"),


]
