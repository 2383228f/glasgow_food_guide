# Generated by Django 2.2.3 on 2020-04-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_userprofile_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.IntegerField(default=55.8642),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.IntegerField(default=-4.2518),
        ),
    ]
