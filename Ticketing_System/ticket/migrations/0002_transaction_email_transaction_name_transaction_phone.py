# Generated by Django 4.0.4 on 2022-06-03 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='email',
            field=models.CharField(default=None, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='name',
            field=models.CharField(default='exit', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
    ]
