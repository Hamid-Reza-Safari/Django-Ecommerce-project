# Generated by Django 5.0.2 on 2024-02-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_is_discount_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_discount',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3, null=True),
        ),
    ]
