# Generated by Django 3.2.8 on 2022-05-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computacao2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='garantia',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.CharField(max_length=10, verbose_name='Marca do produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Produto'),
        ),
    ]
