# Generated by Django 3.2.10 on 2022-12-01 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_auto_20221201_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlaser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 777170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='adminlaser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 777170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 777170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 777170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='clientrep_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 780169, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 783167, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 784166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 784166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 10, 3, 58, 782167, tzinfo=utc)),
        ),
    ]
