# Generated by Django 4.0.3 on 2022-04-06 19:42

from django.db import migrations, models
import enum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fechanac', models.DateField(verbose_name=enum.auto)),
            ],
        ),
    ]
