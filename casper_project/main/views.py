from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница', 'active_home': 'active'})


def order(request):
    return render(request, 'main/order_form.html', {'title': 'Заказ', 'active_order': 'active'})


def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет', 'active_account': 'active'})
# def login(request):
# return render(request, 'main/login.html', {'title': 'Вход'})
# def registration(request):
# return render(request, 'main/reg.html', {'title': 'Регистрация'})
