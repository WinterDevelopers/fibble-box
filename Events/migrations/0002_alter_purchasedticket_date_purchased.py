# Generated by Django 4.0.6 on 2022-07-30 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 17, 45, 41, 950698, tzinfo=utc)),
        ),
    ]