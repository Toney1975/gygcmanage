# Generated by Django 3.1.1 on 2020-10-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20201008_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentfaults',
            name='data_of_failure',
            field=models.DateField(),
        ),
    ]
