# Generated by Django 3.2.9 on 2021-12-07 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211207_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='posted_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]