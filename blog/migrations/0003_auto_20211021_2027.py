# Generated by Django 3.2.7 on 2021-10-21 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_blogcomment_blog_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-date']},
        ),
    ]
