# Generated by Django 3.0 on 2019-12-12 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialieven', '0009_auto_20191211_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overlast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschrijving', models.CharField(max_length=2048)),
                ('activiteit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialieven.Activiteit')),
                ('gebruiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['activiteit'],
            },
        ),
    ]
