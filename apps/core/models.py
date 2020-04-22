from django.db import models

# Event Model
class Event(models.Model):
    user_id = models.IntegerField()
    event_title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    start_dt = models.DateTimeField()
    message = models.CharField(max_length=5000)
    invitee_emails = models.CharField(max_length=5000)
