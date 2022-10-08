from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import RegForm, LoginForm, add_Order, Add_Carrier_Order, UserChangeUpdate
from .models import Order, Order_wait_list
from .service import _order_form_save


def index(request):
    return render(request, 'main/index.html', {'title': 'Transport Support', 'active_home': 'active'})


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


@login_required()
def order(request):
    if request.method == 'POST':
        order_form = add_Order(request.POST)
        if order_form.is_valid():
            _order_form_save(request, order_form)
            messages.success(request, f'Заказ создан!')
            return redirect('home')
        else:
            messages.warning(request, f'Проверьте введенные вами данные!')
            order_form = add_Order(request.POST)
            return render(request, 'main/order_form.html', {'title': 'Заказ', 'active_order': 'active',
                                                            'order_form': order_form})
    else:
        order_form = add_Order()
    return render(request, 'main/order_form.html', {'title': 'Заказ', 'active_order': 'active',
                                                    'order_form': order_form})


@login_required
def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет', 'active_account': 'active'})


def order_list(request):
    paginate_by = 2
    p = Order.objects.all().order_by('-id').exclude(company=request.user).exclude(order_in_w_list__carrier=request.user)
    paginator = Paginator(p, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_paginator = page_obj.has_other_pages()
    if not request.user.is_authenticated:
        messages.warning(request, f'Вам необходимо зарегистрироваться!')
        return redirect('login')
    if not request.user.is_carrier or not request.user.is_verified:
        messages.warning(request, f'Вы не являетесь перевозчиком!')
        return redirect('home')
    if request.method == 'POST':
        form = Add_Carrier_Order(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Заявка оставлена!')
            return redirect('order_list')
        else:
            messages.warning(request, f'Ошибочка повторите попытку!')
            form = Add_Carrier_Order(request.POST)
            return render(request, 'main/order_list.html', {'title': 'Список заказов',
                                                            'active_order_list': 'active',
                                                            'page_obj': page_obj,
                                                            'page_paginator': page_paginator,
                                                            'form': form})
    else:
        form = Add_Carrier_Order()

    return render(request, 'main/order_list.html', {'title': 'Список заказов',
                                                    'active_order_list': 'active',
                                                    'page_obj': page_obj,
                                                    'page_paginator': page_paginator,
                                                    'form': form,
                                                    'query': p})


@login_required
def account_dc(request):
    if request.method == "POST":
        form = UserChangeUpdate(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            messages.success(request, f'Данные сохранены!')
            return redirect('account')
        else:
            messages.warning(request, f'Ошибочка повторите попытку!')
            form = Add_Carrier_Order(request.POST, instance=request.user)
            return render(request, 'main/account_change.html', {
                'title': 'Изменение данных', 'active_account': 'active', 'form': form, })
    else:

        form = UserChangeUpdate(instance=request.user)
        return render(request, 'main/account_change.html', {
            'title': 'Изменение данных', 'active_account': 'active', 'form': form,
        })


@login_required
def your_order_list(request):
    paginate_by = 2
    p = Order.objects.all().order_by('-id').filter(company=request.user)
    paginator = Paginator(p, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_paginator = page_obj.has_other_pages()
    if request.method == 'POST':
        Order.objects.filter(pk=request.POST['order']).delete()
        return render(request, 'main/user_order_list.html', {
            'title': 'Ваши заказы', 'active_account': 'active', 'page_paginator': page_paginator, 'page_obj': page_obj
        })
    return render(request, 'main/user_order_list.html', {
        'title': 'Ваши заказы', 'active_account': 'active', 'page_paginator': page_paginator, 'page_obj': page_obj
    })


def order_detail(request, order_id):
    paginate_by = 2
    query = Order_wait_list.objects.all().order_by('carrier_price').filter(order=order_id)
    paginator = Paginator(query, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_paginator = page_obj.has_other_pages()
    if request.method == 'POST':
        Order.objects.all().filter(pk=order_id).update(carrier=request.POST['carrier'], price=request.POST['price'])
        return redirect('y_o_l')
    return render(request, 'main/order_detail.html', {
            'title': f'заказ №{order_id}', 'active_account': 'active', 'page_paginator': page_paginator, 'page_obj': page_obj
        })
