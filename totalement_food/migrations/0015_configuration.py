# Generated by Django 4.2.dev20230104104714 on 2023-03-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totalement_food', '0014_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('classe', models.CharField(max_length=200)),
            ],
        ),
    ]
