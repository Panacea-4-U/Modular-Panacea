# Generated by Django 3.1.6 on 2022-02-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panacea_app', '0003_auto_20220206_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]