# Generated by Django 2.2.4 on 2019-08-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0002_pais_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='foto',
            field=models.ImageField(blank=True, upload_to='paises'),
        ),
    ]
