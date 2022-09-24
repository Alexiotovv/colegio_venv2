# Generated by Django 2.1 on 2022-07-27 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Curso', '0001_initial'),
        ('Docente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocenteCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
                ('Docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docente.Docente')),
            ],
        ),
    ]
