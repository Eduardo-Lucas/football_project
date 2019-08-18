# Generated by Django 2.2.4 on 2019-08-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Campeonato', max_length=50)),
                ('ano', models.PositiveIntegerField(help_text='Ano em que o Campeonato é disputado')),
                ('ativo', models.BooleanField(default=True, help_text='Indica se o Campeonato está ativo ou não.')),
            ],
        ),
    ]
