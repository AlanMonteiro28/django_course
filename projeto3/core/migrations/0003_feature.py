# Generated by Django 5.1 on 2024-09-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_obj', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('mod_obj', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Dispositivos'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
    ]
