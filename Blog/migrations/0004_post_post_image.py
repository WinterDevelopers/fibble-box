# Generated by Django 4.0.6 on 2022-07-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_insight'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='media/blog/post'),
        ),
    ]
