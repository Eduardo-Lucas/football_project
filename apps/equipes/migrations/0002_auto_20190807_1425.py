# Generated by Django 2.2.4 on 2019-08-07 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipe',
            options={'ordering': ['nome'], 'verbose_name': 'Equipe', 'verbose_name_plural': 'Equipes'},
        ),
    ]