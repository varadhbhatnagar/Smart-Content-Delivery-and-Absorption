from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserLoginForm, UserSignupForm, ProfileForm
from .models import *


class UserSignupFormView(View):
    """!
    @detailed SignUp for User
    """
    user_form_class = UserSignupForm
    profile_form_class = ProfileForm
    template_name = 'registration/registration_form.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        profile_form = self.profile_form_class(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            Profile.objects.create(
                user=user,
                First_Name=profile_form.cleaned_data['First_Name'],
                Last_Name=profile_form.cleaned_data['Last_Name'],
                Role=profile_form.cleaned_data['Role'],
                Class =profile_form.cleaned_data['Class'],
                Subject =profile_form.cleaned_data['Subject'],
                Section =profile_form.cleaned_data['Section']
            )

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class UserLoginFormView(View):
    """!
    @detailed Login for User
    """
    user_form_class = UserLoginForm
    template_name = 'registration/login_form.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request):
        user_form = self.user_form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')

        return render(request, self.template_name, {'user_form': user_form})


def profile(request):
    """!
    @detailed User profile description
    @return path to profile page along with profile information
    """
    my_profile = request.user.profile
    context = {'my_profile': my_profile}
    return render(request, 'SCAD/profile.html', context)

def user_logout(request):
    """!
    @detailed end the sessions for a User
    @return path to home page
    """
    logout(request)
    return redirect('home')

def system_control(request):
    context= {}
    return render(request, 'SCAD/system_control.html', context)

def records(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.pk)

        if profile.Role == 'Teacher':
            subjects = Subject.objects.filter(Teacher = profile.Role)
            context = {'subjects': subjects}
            return render(request, 'SCAD/records.html', context)

        elif profile.Role == 'Student':

            subjects = Subject.objects.filter(Class = profile.Class, Section = profile.Section)
            context = {'subjects': subjects}
            return render(request, 'SCAD/records.html', context)

        elif profile.Role == 'Supervisor':
            subjects = Subject.objects.all()
            context = {'subjects': subjects}
            return render(request, 'SCAD/records.html', context)

        else:
            raise Http404("You can't view this page")
    else:
        redirect('login')


def visualize(request):
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.pk)
        value = []
        label = []

        if profile.Role == 'Teacher':
            subjects = Subject.objects.filter(Teacher = profile.Role)
            context = {'subjects': subjects}
            return render(request, 'SCAD/analysis.html', context)

        elif profile.Role == 'Student':

            subjects = Subject.objects.filter(Class = profile.Class, Section = profile.Section)
            for sub in subjects:
                value.append(0.5 * sub.CA_Score + 0.5 * sub.CD_Score)
                label.append(sub.Subject_Name)
            context = {'value': value, 'label': label}
            return render(request, 'SCAD/analysis.html', context)

        elif profile.Role == 'Supervisor':
            subjects = Subject.objects.all()
            context = {'subjects': subjects}
            return render(request, 'SCAD/analysis.html', context)

        else:
            raise Http404("You can't view this page")
    else:
        redirect('login')

def speechToText(request):
    pass