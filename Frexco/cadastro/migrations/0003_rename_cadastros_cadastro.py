# Generated by Django 4.0.6 on 2022-10-12 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_rename_cadastro_cadastros'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cadastros',
            new_name='Cadastro',
        ),
    ]
