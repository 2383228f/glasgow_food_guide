# Generated by Django 2.2.3 on 2020-04-03 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0019_auto_20200402_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
