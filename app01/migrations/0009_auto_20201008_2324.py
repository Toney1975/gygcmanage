# Generated by Django 3.1.1 on 2020-10-08 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20201008_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrumentfaults',
            old_name='data',
            new_name='databefore',
        ),
    ]