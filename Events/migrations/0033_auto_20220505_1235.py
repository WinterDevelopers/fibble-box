# Generated by Django 3.1.2 on 2022-05-05 12:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0032_auto_20220505_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedticket',
            old_name='serial_number',
            new_name='code',
        ),
        migrations.AddField(
            model_name='purchasedticket',
            name='date_purchased',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 12, 35, 50, 124797, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='purchasedticket',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Events.event'),
        ),
    ]