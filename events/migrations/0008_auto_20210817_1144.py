# Generated by Django 3.2.6 on 2021-08-17 11:44

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210817_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='timezone2',
            field=timezone_field.fields.TimeZoneField(default='Europe/London'),
        ),
        migrations.AlterField(
            model_name='event',
            name='timezone',
            field=models.CharField(default='GMT', max_length=3),
        ),
    ]
