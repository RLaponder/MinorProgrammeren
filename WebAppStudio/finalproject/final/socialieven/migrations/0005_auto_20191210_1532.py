# Generated by Django 3.0 on 2019-12-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialieven', '0004_activiteit_beschrijving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activiteit',
            name='beschrijving',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='categorie',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='datum',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='eindtijd',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='gebouw',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='huisnummer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='plaats',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='postcode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='starttijd',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='straat',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='uitgenodigd',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='verdieping',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]