# Generated by Django 2.2.4 on 2019-08-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Indica o nome do esporte', max_length=50)),
                ('ativo', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, upload_to='esportes')),
            ],
        ),
    ]
