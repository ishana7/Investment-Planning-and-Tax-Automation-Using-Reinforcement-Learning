from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (RegistrationForm, EditProfileForm,)
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def about(request):
    return render(request, 'accounts/about.html')


def whatisai(request):
    return render(request, 'accounts/what-is-ai.html')


def jobloss(request):
    return render(request, 'accounts/job-loss.html')


def incometax(request):
    return render(request, 'accounts/income-tax.html')


def mlai(request):
    return render(request, 'accounts/ml-ai.html')


def neversearchagain(request):
    return render(request, 'accounts/never-search-again.html')


def aivalueprop(request):
    return render(request, 'accounts/ai-value-prop.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/account/home')
            return redirect('/account')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)