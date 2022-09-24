# Generated by Django 2.1 on 2022-07-27 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GradoNivel', models.CharField(default='-', max_length=60)),
                ('Seccion', models.CharField(default='-', max_length=20)),
                ('DNI', models.CharField(max_length=8)),
                ('Direccion', models.CharField(default='', max_length=100)),
                ('FechaNacimiento', models.DateField()),
                ('Sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('Telefono', models.CharField(max_length=60)),
                ('TutorGrado', models.CharField(choices=[('-', '-'), ('1PRIM', '1PRIM'), ('2PRIM', '2PRIM'), ('3PRIM', '3PRIM'), ('4PRIM', '4PRIM'), ('5PRIM', '5PRIM'), ('6PRIM', '6PRIM'), ('1SEC', '1SEC'), ('2SEC', '2SEC'), ('3SEC', '3SEC'), ('4SEC', '4SEC'), ('5SEC', '5SEC')], default='-', max_length=10)),
                ('TutorSeccion', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], default='-', max_length=10)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]