# Generated by Django 2.2.4 on 2019-08-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190818_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
