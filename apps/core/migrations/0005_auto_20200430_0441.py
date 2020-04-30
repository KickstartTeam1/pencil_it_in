# Generated by Django 3.0.5 on 2020-04-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_merge_20200429_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_dt',
            field=models.DateTimeField(help_text='Please select the date and time (displayed in 24-hour format) to END your event.', verbose_name='End Date:'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=128, verbose_name='Name of Event:'),
        ),
        migrations.AlterField(
            model_name='event',
            name='invitee_emails',
            field=models.CharField(help_text="Please use ;'s' to seperate emails addresses.", max_length=5000, verbose_name='Invitee(s) Email Address:'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=256, verbose_name='Event Location:'),
        ),
        migrations.AlterField(
            model_name='event',
            name='message',
            field=models.CharField(help_text='Please enter a message you would like to tell your guests.', max_length=5000, verbose_name='Message:'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_dt',
            field=models.DateTimeField(help_text='Please select the date and time (displayed in 24-hour format) to START your event.', verbose_name='Start Date:'),
        ),
    ]
