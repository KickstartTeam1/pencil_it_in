from django.db import models

from apps.accounts.models import User

# Event Model
class Event(models.Model):
    create_event_user = models.ForeignKey(
       User,
       on_delete=models.CASCADE,
    )
    event_title = models.CharField(max_length=128)
    location = models.CharField(max_length=256)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    message = models.CharField(max_length=5000)
    invitee_emails = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True) # Add current date
    last_modified = models.DateTimeField(auto_now=True)
