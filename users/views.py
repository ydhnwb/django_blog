from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account { username } successfully created! You are now able to login')
            return redirect('users-login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    user_update_form = UserUpdateForm()
    profile_update_form = ProfileUpdateForm()
    context =  {
        'p_form': profile_update_form,
        'u_form': user_update_form
    }
    return render(request, 'users/profile.html', context)

