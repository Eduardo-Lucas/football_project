# Generated by Django 2.2.4 on 2019-08-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0002_auto_20190816_1435'),
        ('equipes', '0005_auto_20190816_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='campeonato',
            field=models.ManyToManyField(to='campeonatos.Campeonato'),
        ),
    ]
