# Generated by Django 2.0.4 on 2019-08-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraiser', '0002_auto_20190801_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventgroupmembers',
            name='is_show_name',
        ),
        migrations.RemoveField(
            model_name='supportgroupmembers',
            name='is_show_name',
        ),
        migrations.AddField(
            model_name='eventgroupmembers',
            name='is_hide_me',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supportgroupmembers',
            name='is_hide_me',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='campaignfundraiser',
            name='sensitivity',
            field=models.CharField(choices=[('high sensitive', 'High'), ('moderate', 'Moderate'), ('charity', 'Charity')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='sensitivity',
            field=models.CharField(choices=[('high sensitive', 'High'), ('moderate', 'Moderate'), ('charity', 'Charity')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='supportgroup',
            name='sensitivity',
            field=models.CharField(choices=[('high sensitive', 'High'), ('moderate', 'Moderate'), ('charity', 'Charity')], max_length=40, null=True),
        ),
    ]