from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm 

# Create your views here.
# message.debug
# message.info
# message.SUCCESS
# message.warning
# message.error


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You ca now login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form' : form}) 

@login_required
def profile(request):
    return render(request, 'profile.html')