from django import forms
from apps.core.models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_title', 'location', 'start_dt', 'end_dt', 'message', 'invitee_emails']

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_title', 'location', 'start_dt', 'end_dt', 'message']