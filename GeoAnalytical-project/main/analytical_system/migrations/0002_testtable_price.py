# Generated by Django 4.0.2 on 2022-03-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytical_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtable',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
