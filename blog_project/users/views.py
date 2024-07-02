from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request):
    """
    This function is used to register a new user. If the request method is POST, the form is validated and saved.
    If the form is valid, the user is redirected to the login page. If the request method is GET, the form is
    displayed.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'{username} was successfully created! Now you can log in into your '
                                              f'account!')
            return redirect('user-login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        }
    return render(request, 'users/register.html', context)


def logout(request):
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, message='your account was successfully updated!')
            return redirect('user-profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
