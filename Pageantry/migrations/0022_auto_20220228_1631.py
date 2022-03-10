# Generated by Django 3.1.2 on 2022-02-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0021_auto_20220227_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponpayment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='couponpayment',
            name='reference',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='couponpayment',
            name='amount',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='couponpayment',
            name='number_of_coupons',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
