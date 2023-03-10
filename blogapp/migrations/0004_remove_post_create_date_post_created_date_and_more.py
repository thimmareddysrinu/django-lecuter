# Generated by Django 4.1.7 on 2023-03-09 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 9, 53, 47, 824950, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 9, 53, 47, 824950, tzinfo=datetime.timezone.utc)),
        ),
    ]
