# Generated by Django 4.2.2 on 2023-06-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecomunicaciones_app', '0002_rename_unidad_capacida_teleco_productoswitchteleco_unidad_capacidad_teleco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productootroteleco',
            name='unidad_garantia',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='productorouterteleco',
            name='unidad_garantia',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='productoswitchteleco',
            name='unidad_garantia',
            field=models.CharField(max_length=20),
        ),
    ]