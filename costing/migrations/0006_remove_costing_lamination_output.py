# Generated by Django 4.1.7 on 2023-03-27 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costing', '0005_costing_lamination_cost_pkg_polly_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costing',
            name='Lamination_OutPut',
        ),
    ]
