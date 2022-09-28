from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import User, Order



class RegForm(UserCreationForm):
    company_type_ = (('ИП', 'ИП'), ('ООО', 'ООО'))
    company_type = forms.CharField(label='Выберите тип организации', widget=forms.Select(choices=company_type_, attrs={
        'class': 'form-select'}))
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
        fields = ('company_type', 'company_name', 'phone', 'email', 'inn')


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class:': 'form_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class:': 'form_input'}))


class add_Order(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
