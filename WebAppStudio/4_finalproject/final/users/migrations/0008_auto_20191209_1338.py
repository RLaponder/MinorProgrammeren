# Generated by Django 3.0 on 2019-12-09 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191205_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='geboortedatum',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='gebouw',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='verdieping',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
