# Generated by Django 3.1.4 on 2020-12-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201223_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
