from django.contrib import admin
from .models import Recette


class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'ingredients', 'valeur_nutri', 'process')
    search_fields = ['titre']


# Register your models here.
admin.site.register(Recette, RecetteAdmin)
