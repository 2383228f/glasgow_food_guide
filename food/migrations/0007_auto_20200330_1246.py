# Generated by Django 2.2.3 on 2020-03-30 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20200330_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_ID',
            new_name='Restaurant_ID',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='email_address',
            new_name='emailAddress',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
    ]