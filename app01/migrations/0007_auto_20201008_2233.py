# Generated by Django 3.1.1 on 2020-10-08 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20201008_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='creater',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='iname',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='intact',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='modifier',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='operation_department',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='work_area',
        ),
        migrations.RemoveField(
            model_name='instrumentfaults',
            name='enforcer',
        ),
        migrations.RemoveField(
            model_name='instrumentfaults',
            name='implentention',
        ),
        migrations.RemoveField(
            model_name='instrumentfaults',
            name='repair_data',
        ),
        migrations.RemoveField(
            model_name='instrumentfaults',
            name='work_order_no',
        ),
    ]