# Generated by Django 3.1.2 on 2022-03-21 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0023_couponpayment_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couponpayment',
            options={'ordering': ['-token']},
        ),
        migrations.AlterField(
            model_name='couponpayment',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='couponpayment',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='pageantrySponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media/sponsors')),
                ('pageantry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pageantry_sponsor', to='Pageantry.pageantry')),
            ],
        ),
    ]
