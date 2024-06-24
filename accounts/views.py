# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Loga o usuário automaticamente após o cadastro
            login(request, user)
            # Redireciona para a página de login
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autentica o usuário
            login(request, form.get_user())
            # Redireciona para a página principal ou outra página desejada
            return redirect('evento_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
        logout(request)
        return redirect('/accounts/login/?next=/') 
