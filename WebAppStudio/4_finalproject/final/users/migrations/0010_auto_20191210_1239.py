# Generated by Django 3.0 on 2019-12-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191209_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='huisnummer',
            field=models.CharField(max_length=6),
        ),
    ]
