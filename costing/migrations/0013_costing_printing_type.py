# Generated by Django 4.1.7 on 2023-03-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costing', '0012_alter_lamination_rate_alter_printing_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='costing',
            name='Printing_Type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
