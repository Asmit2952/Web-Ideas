# Generated by Django 3.2.7 on 2021-09-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]