from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import UserEditForm, SignupForm
from apps.accounts.models import User

#NEW USER SIGN UP 
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away, then redirect home
            messages.success(request, 'Account created successfully. Welcome to Pencil It In!')
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

#LOG IN PAGE
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # User has specified valid credentials, have user log-in, and then
            # redirect back home
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

#LOG OUT PAGE
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('home')

#VIEW PROFILE PAGE
@login_required
def view_profile(request, username):
    user = User.objects.get(username=username)

    if request.user == user:
        is_viewing_self = True
    else:
        is_viewing_self = False

    context = {
        'user': user,
        'is_viewing_self': is_viewing_self,
    }
    return render(request, 'accounts/profile_page.html', context)

#EDIT PROFILE PAGE
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserEditForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)

