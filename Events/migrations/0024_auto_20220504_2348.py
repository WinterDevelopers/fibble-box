# Generated by Django 3.1.2 on 2022-05-04 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0023_auto_20220504_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 23, 48, 51, 12940, tzinfo=utc)),
        ),
    ]