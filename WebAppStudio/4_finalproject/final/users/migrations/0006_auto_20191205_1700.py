# Generated by Django 3.0 on 2019-12-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191205_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Huisnummer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Postcode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Woonplaats',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='straat',
            field=models.CharField(max_length=64, null=True),
        ),
    ]