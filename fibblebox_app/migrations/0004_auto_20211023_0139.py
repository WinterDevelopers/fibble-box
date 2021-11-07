# Generated by Django 3.1.2 on 2021-10-23 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fibblebox_app', '0003_auto_20211023_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_office', to='fibblebox_app.office'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_banner',
            field=models.ImageField(upload_to='media/events'),
        ),
    ]
