# Generated by Django 3.1.2 on 2022-06-20 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]