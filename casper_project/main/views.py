from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница', 'active_home': 'active'})

def register(request):
	if request.method == 'POST':
    	form = UserRegisterForm(request.POST)
    	if form.is_valid():
        	form.save()
        	username = form.cleaned_data.get('username')
        	messages.success(request, f'Создан аккаунт {username}!')
        	return redirect('blog-home')
	else:
    	form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


def order(request):
    return render(request, 'main/order_form.html', {'title': 'Заказ', 'active_order': 'active'})


def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет', 'active_account': 'active'})
# def login(request):
# return render(request, 'main/login.html', {'title': 'Вход'})
# def registration(request):
# return render(request, 'main/reg.html', {'title': 'Регистрация'})
