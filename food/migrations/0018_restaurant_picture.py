# Generated by Django 2.2.3 on 2020-04-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_auto_20200401_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
