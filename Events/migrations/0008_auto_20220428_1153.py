# Generated by Django 3.1.2 on 2022-04-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_auto_20220427_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetails',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Events.order'),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]