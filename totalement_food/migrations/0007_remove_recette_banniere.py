# Generated by Django 4.2.dev20230104104714 on 2023-03-16 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totalement_food', '0006_recette_banniere_alter_recette_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recette',
            name='banniere',
        ),
    ]
