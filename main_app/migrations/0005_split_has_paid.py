# Generated by Django 2.2.9 on 2020-01-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_merge_20200127_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='split',
            name='has_paid',
            field=models.BooleanField(default=False),
        ),
    ]