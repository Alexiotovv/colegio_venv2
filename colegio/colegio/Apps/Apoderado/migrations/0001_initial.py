# Generated by Django 2.1 on 2022-07-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8, unique=True)),
                ('Nombres', models.CharField(max_length=60)),
                ('ApellidoPaterno', models.CharField(max_length=60)),
                ('ApellidoMaterno', models.CharField(max_length=60)),
                ('Direccion', models.CharField(default='', max_length=100)),
                ('Sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('Telefono', models.CharField(max_length=60)),
                ('Email', models.EmailField(max_length=60)),
            ],
        ),
    ]
