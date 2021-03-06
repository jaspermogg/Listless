# Generated by Django 2.0.6 on 2018-07-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_list', '0004_auto_20180701_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Location',
            field=models.DecimalField(decimal_places=2, default=1.1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='PatientPriority',
            field=models.IntegerField(choices=[(1, 'High'), (2, 'Standard'), (3, 'Medically fit for discharge')], default=2),
        ),
    ]
