# Generated by Django 4.1.2 on 2022-12-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_rename_is_bestelling_book_is_bestselling'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
