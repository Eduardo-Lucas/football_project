# Generated by Django 2.2.4 on 2019-08-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20190817_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
