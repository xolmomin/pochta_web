from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput, DateInput, EmailInput, NumberInput

from app.models import Letter
from app.models import Staff


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Parol'}))

    def full_clean(self):
        super().full_clean()

    def clean_username(self):
        username = self.cleaned_data['username']
        if not Staff.objects.filter(username=username).exists():
            raise ValidationError('Login xato')
        return username

    def clean_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not Staff.objects.filter(username=username).exists():
            raise ValidationError('Login xato')

        user = Staff.objects.filter(username=username).first()
        if not user.check_password(password):
            raise ValidationError('Parol xato')
        return password


class CreateBranchForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'phone', 'region', 'address', 'email', 'username', 'password']
        labels = {
            'name': 'FIO',
            'phone': 'Telefon',
            'email': 'Elektron pochta',
            'username': 'Login',
            'password': 'Parol',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'FIO'}),
            'phone': NumberInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),
            'address': TextInput(attrs={'placeholder': 'Manzil'}),
            'email': EmailInput(),
            'username': TextInput(attrs={'placeholder': 'Login'}),
            'password': PasswordInput(attrs={'placeholder': 'Parol'}),
        }
        help_texts = {
            'username': '',
        }


class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'phone', 'region', 'district', 'address', 'email', 'branch', 'username', 'password',
                  'passport_number', 'passport_give_date', 'given_by_whom']
        labels = {
            'username': 'Login',
            'password': 'Parol',
        }
        widgets = {
            # 'name': TextInput(attrs={'placeholder': 'FIO'}),
            # 'phone': TextInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),
            # 'address': TextInput(attrs={'placeholder': 'Manzil'}),
            # 'email': TextInput(attrs={'placeholder': 'Elektron pochta'}),
            'email': EmailInput(),
            'username': TextInput(attrs={'placeholder': 'Login'}),
            'password': PasswordInput(attrs={'placeholder': 'Parol'}),
            'passport_give_date': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
        }
        help_texts = {
            'username': '',
        }


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'inn', 'phone', 'region', 'district', 'company', 'address', 'email', 'branch', 'username',
                  'password', 'bank', 'r_s', 'mfo']
        # labels = {
        #     'name': 'FIO',
        #     'branch': 'Filial',
        #     'email': 'Elektron pochta',
        #     'username': 'Login',
        #     'password': 'Parol',
        # }
        widgets = {
            'phone': NumberInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),

            # 'address': TextInput(attrs={'placeholder': 'Manzil'}),
            # 'email': TextInput(attrs={'placeholder': 'Elektron pochta'}),
            # 'username': TextInput(attrs={'placeholder': 'Login'}),
            # 'password': PasswordInput(attrs={'placeholder': 'Elektron pochta'}),
        }
        help_texts = {
            'username': '',
        }


class CreateLetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['name', 'region', 'district', 'phone', 'address', 'letter_text']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nomi'}),
            'phone': TextInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),
            'address': TextInput(attrs={'placeholder': 'Manzil'}),
        }


class UploadFileForm(forms.Form):
    file = forms.FileField()
