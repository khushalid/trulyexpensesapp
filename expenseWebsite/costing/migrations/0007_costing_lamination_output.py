# Generated by Django 4.1.7 on 2023-03-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costing', '0006_remove_costing_lamination_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='costing',
            name='Lamination_Output',
            field=models.DecimalField(decimal_places=3, max_digits=20, null=True),
        ),
    ]