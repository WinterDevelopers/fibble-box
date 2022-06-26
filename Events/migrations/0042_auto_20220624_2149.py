# Generated by Django 3.1.2 on 2022-06-24 21:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0041_auto_20220624_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='insight',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 21, 49, 22, 354812, tzinfo=utc)),
        ),
    ]
