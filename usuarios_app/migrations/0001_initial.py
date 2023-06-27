# Generated by Django 4.2.2 on 2023-06-27 00:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('nombres', models.CharField(max_length=1000)),
                ('apellidos', models.CharField(max_length=1000)),
                ('correo', models.EmailField(max_length=1000, unique=True)),
                ('username', models.CharField(max_length=1000, unique=True)),
                ('numero_celular', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('foto_perfil', models.ImageField(blank=True, upload_to='imagenes/fotos_perfil')),
            ],
            options={
                'ordering': ['correo'],
            },
        ),
    ]
