# Generated by Django 4.2 on 2023-04-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costing', '0020_costing_poly_cost_costing_poly_qty_costing_poly_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=255, null=True)),
                ('Rate', models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='costing',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
