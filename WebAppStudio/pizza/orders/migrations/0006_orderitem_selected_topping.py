# Generated by Django 2.2.7 on 2019-11-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20191125_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='selected_topping',
            field=models.CharField(default='-', max_length=64),
        ),
    ]