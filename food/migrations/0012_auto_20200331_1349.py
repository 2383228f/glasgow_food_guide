# Generated by Django 2.2.3 on 2020-03-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(),
        ),
    ]