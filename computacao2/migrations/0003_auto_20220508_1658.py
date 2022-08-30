# Generated by Django 3.2.8 on 2022-05-08 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computacao2', '0002_auto_20220508_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='servico',
        ),
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default='', max_length=100, verbose_name='Bairro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(default='', max_length=30, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.CharField(default='', max_length=6, verbose_name='Número'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=100, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=100, verbose_name='Serviço a ser executado')),
                ('data', models.DateTimeField()),
                ('clientname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computacao2.cliente')),
            ],
        ),
    ]
