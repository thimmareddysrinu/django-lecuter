# Generated by Django 4.1.7 on 2023-03-09 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_remove_post_create_date_post_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 10, 10, 51, 336378, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 10, 10, 51, 336378, tzinfo=datetime.timezone.utc)),
        ),
    ]