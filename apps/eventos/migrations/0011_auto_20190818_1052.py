# Generated by Django 2.2.4 on 2019-08-18 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0010_evento_concurso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='nova_data',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='placar_coluna_1',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='placar_coluna_2',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='status',
        ),
    ]
