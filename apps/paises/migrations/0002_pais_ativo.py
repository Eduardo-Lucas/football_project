# Generated by Django 2.2.4 on 2019-08-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
