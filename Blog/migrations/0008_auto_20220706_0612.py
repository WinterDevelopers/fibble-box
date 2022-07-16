# Generated by Django 3.2.9 on 2022-07-06 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0026_auto_20220419_2034'),
        ('Blog', '0007_auto_20220701_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_published']},
        ),
        migrations.AddField(
            model_name='post',
            name='last_updated',
            field=models.DateField(auto_now=True, verbose_name='Last Updated'),
        ),
        migrations.AddField(
            model_name='writer',
            name='d_o_b',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='writer',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='bio',
            field=models.TextField(help_text='About yourself'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pageantry.user'),
        ),
    ]