# Generated by Django 5.0.2 on 2024-02-27 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_sale',
            new_name='is_discount',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sale_price',
            new_name='sale_discount',
        ),
    ]