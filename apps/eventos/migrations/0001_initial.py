# Generated by Django 2.2.4 on 2019-08-17 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divisoes', '0001_initial'),
        ('equipes', '0009_remove_equipe_divisao'),
        ('rodadas', '0003_auto_20190817_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Informa a data em que o evento vai ocorrer')),
                ('hora', models.DateField(help_text='Informa a hora em que o evento vai ocorrer')),
                ('status', models.CharField(choices=[('Normal', 'normal'), ('Adiado', 'adiado'), ('Cancelado', 'cancelado')], default='normal', max_length=20)),
                ('nova_data', models.DateField(blank=True, help_text='Informa a nova data, no caso de evento adiado', null=True)),
                ('divisao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisoes.Divisao')),
                ('equipe_coluna_1', models.ForeignKey(help_text='Indica o dono da casa', on_delete=django.db.models.deletion.CASCADE, related_name='mandante', to='equipes.Equipe')),
                ('equipe_coluna_2', models.ForeignKey(help_text='Indica o visitante', on_delete=django.db.models.deletion.CASCADE, related_name='visitante', to='equipes.Equipe')),
                ('rodada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rodadas.Rodada')),
            ],
        ),
    ]
