from django.shortcuts import render, redirect
from django import forms
from apps.core.models import Event


class CreateEventForm(forms.Form):
    user_id = forms.IntegerField()
    event_title = forms.CharField(max_length=128)
    location = forms.CharField(max_length=128)
    date = forms.DateTimeField()
    message = forms.CharField(max_length=5000)
    invites = forms.CharField(max_length=5000)

# Two example views. Change or delete as necessary.
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
            user_id = form.cleaned_data['user_id']
            title = form.cleaned_data['event_title']
            location = form.cleaned_data['location']
            date = form.cleaned_data['date']
            message = form.cleaned_data['message']
            invites = form.cleaned_data['invites']

            Event.objects.create(
                user_id=user_id,
                event_title=title,
                location=location,
                start_dt=date,
                message=message,
                invitee_emails=invites,
            )

            return redirect('/')
    else:
        form = CreateEventForm()
    
    context = {
        'form': form,
    }

    return render(request, 'pages/create_form.html', context)