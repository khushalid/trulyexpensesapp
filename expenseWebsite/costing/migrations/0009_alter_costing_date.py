# Generated by Django 4.1.7 on 2023-03-27 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costing', '0008_costing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costing',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]