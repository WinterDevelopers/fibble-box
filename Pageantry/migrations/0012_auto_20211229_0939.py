# Generated by Django 3.1.2 on 2021-12-29 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pageantry', '0011_event_event_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pageantry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('pageantry_image', models.ImageField(upload_to='media/pageantry')),
                ('pageantry_banner', models.ImageField(upload_to='media/pageantry')),
                ('pageantry_info', models.CharField(blank=True, max_length=3000, null=True)),
                ('category', models.CharField(choices=[('pg', 'pagentry'), ('aw', 'awards'), ('su', 'survey'), ('cm', 'comperism')], max_length=2, null=True)),
                ('intro_text', models.CharField(max_length=250, null=True)),
                ('discription', models.CharField(max_length=450, null=True)),
                ('date', models.DateField()),
                ('count_down', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='event',
        ),
        migrations.RemoveField(
            model_name='office',
            name='event',
        ),
        migrations.RemoveField(
            model_name='votingcode',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='candidate',
            name='pageantry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pageantry_candidate', to='Pageantry.pageantry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='office',
            name='pageantry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pageantry_office', to='Pageantry.pageantry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votingcode',
            name='pageantry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pageantry_code', to='Pageantry.pageantry'),
            preserve_default=False,
        ),
    ]