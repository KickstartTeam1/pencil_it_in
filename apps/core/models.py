from django.db import models
from datetime import datetime

from apps.accounts.models import User

# Event Model
class Event(models.Model):
    create_event_user = models.ForeignKey(
       User,
       on_delete=models.CASCADE, default=99999999
    )
    event_title = models.CharField(verbose_name="Name of Event:", max_length=128)
    location = models.CharField(verbose_name="Event Location:", max_length=256)
    start_dt = models.DateTimeField(verbose_name="Start Date:", help_text="Select the date and time (displayed in 24-hour format) to START your event.")
    end_dt = models.DateTimeField(verbose_name="End Date:", help_text="Select the date and time (displayed in 24-hour format) to END your event.")
    message = models.CharField(verbose_name="Message:", max_length=5000, help_text="Enter a message you would like to tell your guests.")
    invitee_emails = models.CharField(verbose_name="Invitee(s) Email Address:", max_length=5000, help_text="Use ' ; ' to seperate email addresses.")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
