# Generated by Django 4.2.3 on 2023-11-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBiblio', '0004_livro_exemplares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichaemprestimo',
            name='devolucao',
            field=models.DateField(blank=True),
        ),
    ]