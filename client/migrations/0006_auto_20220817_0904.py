# Generated by Django 3.2.10 on 2022-08-17 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20220815_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlaser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='adminlaser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobstatus',
            name='jobstatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 8, 4, 7, 218862, tzinfo=utc)),
        ),
    ]
