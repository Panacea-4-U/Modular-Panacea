# Generated by Django 3.1.6 on 2022-02-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panacea_app', '0002_auto_20220206_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempdb',
            name='ph_no',
            field=models.CharField(max_length=15),
        ),
    ]
