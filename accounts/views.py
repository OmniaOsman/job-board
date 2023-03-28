from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile/')
    else:
        form = SignupForm()
        
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(request.POST, request.FILES, instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myProfile = profileForm.save(commit=False)
            myProfile.user = request.user
            myProfile.save()
            return redirect(reverse('accounts:profile'))
        pass
    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)
        
    context = {'userForm': userForm, 'profileForm': profileForm}
    return render(request, 'accounts/profile_edit.html', context)