# Generated by Django 3.2.8 on 2022-05-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computacao2', '0006_servicos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='valornota',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10, verbose_name='Valor total da nota'),
        ),
    ]
