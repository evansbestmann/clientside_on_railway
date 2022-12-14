# Generated by Django 3.2.10 on 2022-12-14 08:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20221213_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='copied_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='adminlaser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 114489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='adminlaser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 114489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 114489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 114489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='clientrep_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 114489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 130131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 130131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 130131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 43, 58, 114489, tzinfo=utc)),
        ),
    ]
