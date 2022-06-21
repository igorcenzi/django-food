# Generated by Django 4.0.5 on 2022-06-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(related_name='ingredients', to='recipes.recipe'),
        ),
    ]