# Generated by Django 2.0.6 on 2018-06-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_list', '0002_auto_20180630_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
    ]
