# Generated by Django 4.2.dev20230104104714 on 2023-03-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totalement_food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='photo',
            field=models.CharField(max_length=200),
        ),
    ]