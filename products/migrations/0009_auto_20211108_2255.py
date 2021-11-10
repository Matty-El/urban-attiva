# Generated by Django 3.2.7 on 2021-11-08 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='Minimum of 50 characters required', max_length=2000, null=True, validators=[django.core.validators.RegexValidator(message='Please only use text and numbers and common punctuation characters', regex='^[a-zA-Z0-9,!?\\.\\(\\)@"\\\'# -]+$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Minimum of 10 characters required', max_length=254, validators=[django.core.validators.RegexValidator(message='Please only use text and numbers and common punctuation characters', regex='^[a-zA-Z0-9,!?\\.\\(\\)"\\\' -]+$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]