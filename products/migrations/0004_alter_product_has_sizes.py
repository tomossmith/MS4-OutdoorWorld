# Generated by Django 3.2 on 2022-02-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_sizes',
            field=models.CharField(choices=[('clothing', 'Clothing'), ('footwear', 'Footwear'), ('no-sizes', 'No Sizing')], default='no-sizing', max_length=15),
        ),
    ]
