# Generated by Django 3.0.3 on 2020-03-03 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200303_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date_posted',
            new_name='event_date',
        ),
    ]