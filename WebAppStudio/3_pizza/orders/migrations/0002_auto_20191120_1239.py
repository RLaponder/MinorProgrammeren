# Generated by Django 2.2.7 on 2019-11-20 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dinnerplatters',
            new_name='dinnerplatter',
        ),
        migrations.RenameModel(
            old_name='salads',
            new_name='salad',
        ),
        migrations.RenameModel(
            old_name='subs',
            new_name='sub',
        ),
        migrations.RenameModel(
            old_name='toppings',
            new_name='topping',
        ),
    ]
