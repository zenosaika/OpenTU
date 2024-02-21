from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Welcome {username}!')
                return redirect('/dashboard')
        messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'User/login.html', {'login_form':form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Logout Successful.')
    return redirect('/')