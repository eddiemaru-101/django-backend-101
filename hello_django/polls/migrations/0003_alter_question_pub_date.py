# Generated by Django 5.1.7 on 2025-03-26 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 26, 11, 33, 47, 861122, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
