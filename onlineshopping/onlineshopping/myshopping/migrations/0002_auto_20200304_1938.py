# Generated by Django 3.0.3 on 2020-03-04 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brands',
            new_name='Brand',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]