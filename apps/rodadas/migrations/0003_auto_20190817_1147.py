# Generated by Django 2.2.4 on 2019-08-17 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0003_auto_20190816_1615'),
        ('rodadas', '0002_auto_20190817_1134'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rodada',
            unique_together={('campeonato', 'numero')},
        ),
    ]
