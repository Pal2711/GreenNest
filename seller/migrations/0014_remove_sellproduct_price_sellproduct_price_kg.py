# Generated by Django 4.2.16 on 2025-06-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0013_rename_quantity_sellproduct_quantity_kg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellproduct',
            name='price',
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='price_kg',
            field=models.IntegerField(null=True),
        ),
    ]
