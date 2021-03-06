from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from apps.core.models import Event
from apps.core.forms import CreateEventForm, EditEventForm
from apps.core.email import Email
from datetime import datetime

def home(request):
    context = {}

    return render(request, 'pages/home.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        logged_in_user = request.user
        if form.is_valid():
            event = form.save(commit=False)
            event.create_event_user = logged_in_user
            event.save()

            email_successful = Email.create_email(event.id, logged_in_user.id)
            if email_successful:
                messages.success(request, 'Successful email send!')
            else:
                messages.success(request, 'Failed email send!')

            return redirect('../../account/users/' + request.user.username)

    else:
        form = CreateEventForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/create_form.html', context)

@login_required
def edit_event(request, event_id):
    # Get the event we are looking for
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = EditEventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            messages.success(request, 'Event update successful.')
            return redirect('../../account/users/' + request.user.username)

    else:
        # A GET, create a pre-filled form with the instance.
        form = EditEventForm(instance=event)

    context = {
        'form': form,
    }
    return render(request, 'pages/edit_event.html', context)

def event(request, event_id):
    event = Event.objects.get(id=event_id)

    context = {
        'event_title': event.event_title,
        'location': event.location,
        'start': event.start_dt,
        'end': event.end_dt,
        'message': event.message,
    }

    return render(request, 'pages/event_receipt.html', context)
