# Generated by Django 3.2.7 on 2021-10-30 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211030_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parent_category',
        ),
    ]
