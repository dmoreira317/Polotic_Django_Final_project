# Generated by Django 3.2.4 on 2021-06-18 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete01', '0004_remove_producto_categoria_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria_base',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jaguarete01.categoria'),
        ),
    ]
