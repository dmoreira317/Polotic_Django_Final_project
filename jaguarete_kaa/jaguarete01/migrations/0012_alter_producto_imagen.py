# Generated by Django 3.2.4 on 2021-06-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete01', '0011_remove_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='uploaded_images'),
        ),
    ]
