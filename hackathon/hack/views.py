from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile


def index(request):
    nom = Profile.objects.all()
    nav1 = "active"
    return render(request, 'hack/index.html', {'nom':nom, 'nav1':nav1})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.address = form.cleaned_data.get('address')
            # user.profile.pan_number = form.cleaned_data.get('pan_number')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.profile.email_id = form.cleaned_data.get('email_id')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.profile_pic = form.cleaned_data.get('profile_pic')
            # user.profile.referal_id = form.cleaned_data.get('referal_id')
            user.profile.mobile_number = form.cleaned_data.get('mobile_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    rnav = "active"
    return render(request, 'hack/signup.html', {'form':form, 'rnav':rnav})


def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('home')
    else:
        return HttpResponseRedirect('/invalid/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def log_in(request):
    lnav = "active"
    return render(request, 'hack/login.html', {'lnav':lnav})


def change_password(request):
    value2 = "active"
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'hack/change_password.html', {'form': form, 'value2':value2})
