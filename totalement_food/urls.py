
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('recette', views.la_recette, name="la_recette"),


]
