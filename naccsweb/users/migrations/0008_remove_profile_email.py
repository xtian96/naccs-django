# Generated by Django 2.2.4 on 2019-08-13 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
