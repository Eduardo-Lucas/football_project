# Generated by Django 2.2.4 on 2019-08-17 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_auto_20190817_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nova_data',
            field=models.DateTimeField(blank=True, help_text='Informa a nova data e hora, no caso de evento adiado', null=True),
        ),
    ]
