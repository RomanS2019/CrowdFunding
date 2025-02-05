# Generated by Django 2.0.4 on 2019-08-22 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundraiser', '0003_auto_20190808_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='Banner')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_edited', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
