# Generated by Django 3.2.4 on 2021-06-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete01', '0013_producto_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
