# Generated by Django 2.2.4 on 2019-08-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name': 'Jogador', 'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AddField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(blank=True, upload_to='jogadores'),
        ),
    ]
