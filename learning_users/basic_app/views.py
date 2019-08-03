from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    base_dict = {'base_title': "BASE PAGE"}
    return render(request, "basic_app/base.html",context=base_dict)


def index(request):
    index_dict = {'index_title': "INDEX PAGE"}
    return render(request, "basic_app/index.html",context=index_dict)

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username") # Name mentioned in HTML Tag
        password = request.POST.get("password") # Name mentioned in HTML Tag
        user =authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect("Account not active")
        else:
            print("someone tried to login and failed")
            print("Username {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'basic_app/login.html', {})

    # login_form = UserForm()
    # login_dict = {'login_title': "LOGIN PAGE", 'login_form': login_form}
    return render(request, "basic_app/login.html",context=login_dict)


def registration(request):
    registered = False
    if request.method == "POST":
        login_form = UserForm(data=request.POST)
        registration_form = UserProfileInfoForm(data=request.POST)
        if login_form.is_valid() and registration_form.is_valid():
            user = login_form.save()
            # It is make aware django that it need to use password algoridthm mentioned in
            # settings.py
            user.set_password(user.password)
            user.save()

            profile = registration_form.save(commit=False)
            # Make a relationship that user in login_form is same as registration_form
            profile.user = user
            if 'profile_pic' == request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(login_form.errors, registration_form.errors)
    else:
        login_form = UserForm()
        registration_form = UserProfileInfoForm()
    registration_dict = {'registration_title': "REGISTRATION PAGE", 'login_form': login_form, 'registration_form': registration_form, 'registered': registered}
    return render(request, "basic_app/registration.html",context=registration_dict)
