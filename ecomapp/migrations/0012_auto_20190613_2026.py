# Generated by Django 2.2.2 on 2019-06-13 20:26

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0011_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=ecomapp.models.image_folder),
        ),
    ]
