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
    titre = models.CharField(max_length=200)
    definition = models.TextField(null=True)

    def __str__(self):
        return self.titre


class Ingredients(models.Model):
    nom = models.CharField(max_length=200)
    energie = models.CharField(max_length=10)
    proteine = models.CharField(max_length=10)
    lipide = models.CharField(max_length=10)
    glucide = models.CharField(max_length=10)

    def __str__(self):
        return self.nom


# class Configuration(models.Model):

#     nom = models.CharField(max_length=200)
#     classe = models.CharField(max_length=200)

#     def __str__(self):
#         return self.nom
