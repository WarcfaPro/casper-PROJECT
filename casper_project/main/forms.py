from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User


class RegForm(UserCreationForm):
    company_type_ = (('ИП', 'ИП'), ('ООО', 'ООО'))
    company_type = forms.CharField(label='Выберите тип организации', widget=forms.Select(choices=company_type_, attrs={
        'class:': 'form_input form_multibox'}))
    company_name = forms.CharField(label='Введите название организации',
                                   widget=forms.TextInput(attrs={'class:': 'form_input'}))
    email = forms.EmailField(label='Введите email', widget=forms.EmailInput(attrs={'class:': 'form_input'}))
    phone = forms.CharField(label='Введите телефон', widget=forms.TextInput(attrs={'class:': 'form_input'}))
    inn = forms.CharField(label='Введите ИНН организации',
                          widget=forms.TextInput(attrs={'class:': 'form_input', 'minlength': '10', 'maxlength': '12'}))
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class:': 'form_input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class:': 'form_input'}))

    class Meta:
        model = User
        fields = ('company_type', 'company_name', 'phone', 'email', 'inn')


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
