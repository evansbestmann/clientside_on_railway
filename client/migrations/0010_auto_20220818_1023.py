# Generated by Django 3.2.10 on 2022-08-18 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20220817_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlaser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 82398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='adminlaser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 82398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 82398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 82398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 82398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='analysis_and_report',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='complaint_response',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 98023, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='job_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='job_schedule',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='recommend_us',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='staff_performance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 98023, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 98023, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 9, 23, 46, 98023, tzinfo=utc)),
        ),
    ]
