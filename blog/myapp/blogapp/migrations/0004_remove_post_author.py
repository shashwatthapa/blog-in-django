# Generated by Django 5.1.3 on 2024-11-24 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
