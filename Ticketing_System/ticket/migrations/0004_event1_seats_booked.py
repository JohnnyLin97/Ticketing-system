# Generated by Django 4.0.4 on 2022-06-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_rename_seats_event1_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='event1_seats',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
