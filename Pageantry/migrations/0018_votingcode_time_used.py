# Generated by Django 3.1.2 on 2022-02-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0017_remove_votingcode_pageantry'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingcode',
            name='time_used',
            field=models.DateTimeField(null=True),
        ),
    ]
