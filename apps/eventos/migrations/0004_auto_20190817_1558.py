# Generated by Django 2.2.4 on 2019-08-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_evento_ativo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['sequencia']},
        ),
        migrations.AddField(
            model_name='evento',
            name='sequencia',
            field=models.PositiveIntegerField(default=1, help_text='Indica o número do evento na rodada'),
            preserve_default=False,
        ),
    ]
