# Generated by Django 3.1.2 on 2022-01-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0014_auto_20220108_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reference',
            field=models.CharField(max_length=100, null=True),
        ),
    ]