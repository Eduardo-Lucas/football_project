# Generated by Django 2.2.4 on 2019-08-17 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concursos', '0001_initial'),
        ('eventos', '0009_auto_20190817_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='concurso',
            field=models.ForeignKey(default=864, on_delete=django.db.models.deletion.CASCADE, to='concursos.Concurso'),
            preserve_default=False,
        ),
    ]
