# Generated by Django 3.1.2 on 2022-05-04 23:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0025_auto_20220504_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 23, 50, 6, 879313, tzinfo=utc)),
        ),
    ]