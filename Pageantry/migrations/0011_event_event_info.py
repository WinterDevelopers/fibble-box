# Generated by Django 3.1.2 on 2021-11-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0010_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_info',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
