# Generated by Django 3.0.8 on 2020-08-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.TextField()),
                ('nombre', models.TextField()),
                ('horas', models.TextField()),
                ('creditos', models.TextField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
