# Generated by Django 2.2.4 on 2019-09-02 11:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 11, 53, 4, 839922, tzinfo=utc)),
        ),
    ]