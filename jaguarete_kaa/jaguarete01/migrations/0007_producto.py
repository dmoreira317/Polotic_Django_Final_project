# Generated by Django 3.2.4 on 2021-06-18 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete01', '0006_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('categoria', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('imagen', models.FileField(upload_to='')),
                ('fecha_creacion', models.DateTimeField()),
                ('categoria_base', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jaguarete01.categoria')),
            ],
        ),
    ]