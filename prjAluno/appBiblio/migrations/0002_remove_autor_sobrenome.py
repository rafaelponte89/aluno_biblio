# Generated by Django 4.2.3 on 2023-11-06 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBiblio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='sobrenome',
        ),
    ]
