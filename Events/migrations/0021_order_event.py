# Generated by Django 3.1.2 on 2022-05-01 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0020_remove_order_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Events.event'),
        ),
    ]
