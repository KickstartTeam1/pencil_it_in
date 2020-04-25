from django.shortcuts import render, redirect
from django import forms
from apps.core.models import Event
from apps.core.forms import CreateEventForm, EditEventForm

from datetime import datetime

now = datetime.now()
print(now)

#24-hour format
print(now.strftime('%Y/%m/%d %H:%M:%S'))

#12-hour format
print(now.strftime('%m/%d/%Y %I:%M:%S'))

print(now.strftime('%m/%d/%Y %I:%M %p'))

#I is 12 hour time, p is am/pm
print(now.strftime('%I:%M %p'))


# class CreateEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['event_title', 'location', 'start_dt', 'message', 'invitee_emails']

# class EditEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['event_title', 'location', 'start_dt', 'message']


def home(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }

    return render(request, 'pages/home.html', context)

def create_event(request):
    if request.method == 'POST':

        form = CreateEventForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = CreateEventForm()
    
    context = {
        'form': form,
    }

    return render(request, 'pages/create_form.html', context)

def edit_event(request, event_id):
    # Get the event we are looking for
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = EditEventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        # A GET, create a pre-filled form with the instance.
        form = EditEventForm(instance=event)

    context = {
        'form': form,
    }
    return render(request, 'pages/edit_event.html', context)