# Generated by Django 3.2.9 on 2022-07-16 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0054_alter_purchasedticket_date_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 16, 10, 53, 15, 390494, tzinfo=utc)),
        ),
    ]
