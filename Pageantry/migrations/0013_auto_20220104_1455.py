# Generated by Django 3.1.2 on 2022-01-04 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0012_auto_20211229_0939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ('date_of_transaction',)},
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='date_of_transaction',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='pageantry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pageantry_candidate', to='Pageantry.pageantry'),
        ),
        migrations.AlterField(
            model_name='pageantry',
            name='intro_text',
            field=models.CharField(default='default text', max_length=250),
        ),
        migrations.AlterField(
            model_name='pageantry',
            name='name',
            field=models.CharField(default='default text', max_length=250),
        ),
        migrations.AlterField(
            model_name='pageantry',
            name='pageantry_info',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='pageantry',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pageantry.candidate'),
        ),
        migrations.AlterField(
            model_name='votingcode',
            name='pageantry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pageantry_code', to='Pageantry.pageantry'),
        ),
    ]
