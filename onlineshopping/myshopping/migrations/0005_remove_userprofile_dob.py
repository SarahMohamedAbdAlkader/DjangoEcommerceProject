# Generated by Django 3.0.3 on 2020-03-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0004_auto_20200320_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='DOB',
        ),
    ]
