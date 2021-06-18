# Generated by Django 3.2.4 on 2021-06-18 16:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='titulo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria_base',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jaguarete01.categoria'),
            preserve_default=False,
        ),
    ]