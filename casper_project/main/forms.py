from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Order, Order_wait_list


class RegForm(UserCreationForm):
    company_name = forms.CharField(label='Введите название организации',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Введите email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Введите телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    inn = forms.CharField(label='Введите ИНН организации',
                          widget=forms.TextInput(attrs={'class': 'form-control', 'minlength': '10', 'maxlength': '12'}))
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('inn', 'company_name', 'phone', 'email')


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form_input'}))


class add_Order(forms.ModelForm):
    company_name = forms.CharField(label='Название организации', max_length=100)
    address_city = forms.CharField(label='Город от куда ', max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'id': 'city', 'class': 'form_input'}))
    address_street = forms.CharField(label='Улица', max_length=100, required=False,
                                     widget=forms.TextInput(attrs={'id': 'street', 'class': 'form_input'}))
    address_city_to = forms.CharField(label='Город куда', max_length=50,
                                      widget=forms.TextInput(attrs={'id': 'city_to', 'class': 'form_input'}))
    address_street_to = forms.CharField(label='Улица', max_length=100, required=False,
                                        widget=forms.TextInput(
                                            attrs={'id': 'street_to', 'class': 'form_input'}))
    price = forms.CharField(label='стоимость', max_length=100)

    class Meta():
        model = Order
        fields = ('company_name', 'address_city', 'address_street', 'address_city_to', 'address_street_to', 'price')


class UserChangeUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone')


class Add_Carrier_Order(forms.ModelForm):
    queryset_o = Order.objects.all().filter()
    queryset_c = User.object.all().filter()
    order = forms.ModelChoiceField(queryset=queryset_o, widget=forms.HiddenInput())
    carrier = forms.ModelChoiceField(queryset=queryset_c, widget=forms.HiddenInput())
    carrier_price = forms.DecimalField(label='Ваша цена', max_digits=19, decimal_places=0)

    def __init__(self, *args, **kwargs):
        super(Add_Carrier_Order, self).__init__(*args, **kwargs)
        self.fields['order'].widget.attrs.update({
            'value': '{{item}}'
        })

    class Meta:
        model = Order_wait_list
        fields = ('order', 'carrier', 'carrier_price')
