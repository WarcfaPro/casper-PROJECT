from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegForm, LoginForm, add_Order


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница', 'active_home': 'active'})


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Вы уже вошли!')
        return redirect('home')
    if request.method == 'POST':
        user_form = RegForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            company_name = user_form.cleaned_data.get('company_name')
            messages.success(request, f'Создан аккаунт {company_name}!')
            cd = user_form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        user_form = RegForm()
    return render(request, 'main/register.html', {'user_form': user_form, 'active_reg': 'active'})


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Вы уже вошли!')
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, f'Проверьте введенные вами данные!')
                form = LoginForm()
                return render(request, 'main/login.html', {'form': form, 'active_login': 'active'})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form, 'active_login': 'active'})


def logout_user(request):
    logout(request)
    return redirect('home')


def order(request):
    order_form = add_Order()
    return render(request, 'main/order_form.html', {'title': 'Заказ', 'active_order': 'active', 'order_form': order_form})


def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет', 'active_account': 'active'})
