# Generated by Django 3.1.4 on 2020-12-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201209_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_name',
            new_name='name',
        ),
    ]
