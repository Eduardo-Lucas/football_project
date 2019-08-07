# Generated by Django 2.2.4 on 2019-08-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipes', '0002_auto_20190807_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('posicao', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('local_nascimento', models.CharField(blank=True, max_length=50, null=True)),
                ('pais', models.CharField(blank=True, max_length=20, null=True)),
                ('chuta_com_pe', models.CharField(choices=[('Direito', 'Direito'), ('Esquerdo', 'Esquerdo')], default='Direito', max_length=10)),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('altura', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('numero_camisa', models.PositiveIntegerField(blank=True, null=True)),
                ('em_atividade', models.BooleanField(default=True)),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipes.Equipe')),
            ],
        ),
    ]
