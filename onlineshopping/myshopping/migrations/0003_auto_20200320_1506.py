# Generated by Django 3.0.3 on 2020-03-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0002_auto_20200320_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]
