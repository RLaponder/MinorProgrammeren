# Generated by Django 2.2.7 on 2019-11-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_addition'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
            preserve_default=False,
        ),
    ]
