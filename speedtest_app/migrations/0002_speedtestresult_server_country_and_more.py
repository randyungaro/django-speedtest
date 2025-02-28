# Generated by Django 5.1.6 on 2025-02-17 05:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("speedtest_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="speedtestresult",
            name="server_country",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="speedtestresult",
            name="server_location",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="speedtestresult",
            name="server_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="speedtestresult",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
