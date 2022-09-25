from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import RegForm, LogForm
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница', 'active_home': 'active'})


def register(request):
    if request.method == 'POST':
        user_form = RegForm(data=request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            user_form.save()
            company_name = user_form.cleaned_data.get('company_name')
            messages.success(request, f'Создан аккаунт {company_name}!')
            return redirect('home')
    else:
        user_form = RegForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def login(request):
    if request.method == 'POST':
        user_loginform = LogForm(data=request.POST)
        if user_loginform.is_valid():
            # Create a new user object but avoid saving it yet
            user_loginform.save()
            company_name = user_loginform.cleaned_data.get('company_name')
            messages.success(request, f'Создан аккаунт {company_name}!')
            return redirect('home')
    else:
        user_loginform = LogForm()
    return render(request, 'main/login.html', {'user_form': user_loginform})


def logout_user(request):
    logout(request)
    return redirect('home')


def order(request):
    return render(request, 'main/order_form.html', {'title': 'Заказ', 'active_order': 'active'})


def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет', 'active_account': 'active'})
# def login(request):
# return render(request, 'main/login.html', {'title': 'Вход'})
# def registration(request):
# return render(request, 'main/reg.html', {'title': 'Регистрация'})