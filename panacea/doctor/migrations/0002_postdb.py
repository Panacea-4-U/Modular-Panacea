# Generated by Django 3.1.6 on 2022-04-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'postdb',
            },
        ),
    ]
