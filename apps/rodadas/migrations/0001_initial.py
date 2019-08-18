# Generated by Django 2.2.4 on 2019-08-17 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campeonatos', '0003_auto_20190816_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rodada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(help_text='Indica o número da Rodada', max_length=2)),
                ('ativo', models.BooleanField(default=True)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonatos.Campeonato')),
            ],
            options={
                'ordering': ['campeonato', 'numero', '-ativo'],
            },
        ),
    ]
