# Generated by Django 4.0.6 on 2022-10-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('senha', models.CharField(blank=True, max_length=255)),
                ('data_nasc', models.DateField()),
            ],
        ),
    ]
