# Generated by Django 5.0.2 on 2024-02-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_is_sale_product_is_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
    ]