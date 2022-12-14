# Generated by Django 3.2.10 on 2022-12-13 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20221213_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlaser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 670546, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='adminlaser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 670546, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 670546, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 670546, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 673544, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedbackclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 675543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 676543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notificationclient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 676543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 9, 55, 3, 674544, tzinfo=utc)),
        ),
    ]
