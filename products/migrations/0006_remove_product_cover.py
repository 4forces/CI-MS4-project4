# Generated by Django 3.1.4 on 2020-12-17 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cover',
        ),
    ]
