# Generated by Django 4.1.7 on 2023-03-10 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_alter_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
