# Generated by Django 3.1.2 on 2022-06-20 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.post'),
        ),
    ]
