# Generated by Django 4.0.6 on 2022-07-30 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0052_alter_purchasedticket_date_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 16, 46, 24, 6566, tzinfo=utc)),
        ),
    ]
