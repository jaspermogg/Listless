# Generated by Django 2.0.6 on 2018-07-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_list', '0005_auto_20180701_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Location',
        ),
        migrations.AddField(
            model_name='patient',
            name='LocationBay',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='LocationBed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]