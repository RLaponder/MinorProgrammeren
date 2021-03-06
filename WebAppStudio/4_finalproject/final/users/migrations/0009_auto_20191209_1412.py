# Generated by Django 3.0 on 2019-12-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191209_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='huisnummer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='postcode',
            field=models.CharField(default='1234ab', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='straat',
            field=models.CharField(default='maassluisstraat', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='woonplaats',
            field=models.CharField(default='amsterdam', max_length=64),
            preserve_default=False,
        ),
    ]
