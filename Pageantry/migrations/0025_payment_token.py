# Generated by Django 3.1.2 on 2022-03-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0024_auto_20220321_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='token',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
