# Generated by Django 5.0.2 on 2024-03-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
