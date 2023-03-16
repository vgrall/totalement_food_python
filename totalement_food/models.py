from django.db import models


class Recette(models.Model):
    titre = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)
    valeur_nutri = models.CharField(max_length=500)
    process = models.TextField()
    photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    entree = models.CharField(max_length=200)
    plat = models.CharField(max_length=200)
    dessert = models.CharField(max_length=200)
