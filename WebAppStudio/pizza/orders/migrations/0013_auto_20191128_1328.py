# Generated by Django 2.2.7 on 2019-11-28 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20191128_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item_price',
            new_name='price',
        ),
    ]