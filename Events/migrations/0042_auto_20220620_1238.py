# Generated by Django 3.1.2 on 2022-06-20 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0041_auto_20220620_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 11, 38, 1, 900259, tzinfo=utc)),
        ),
    ]
