from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from app.models import Region, District, Letter, Staff


class CreateLetterForm(forms.ModelForm):
    region = forms.ModelChoiceField(label='Viloyat', queryset=Region.objects.all())
    district = forms.ModelChoiceField(label='Tuman', queryset=District.objects.all())
    letter_text = forms.CharField(label='Xat yozish', widget=CKEditorUploadingWidget())

    class Meta:
        model = Letter
        fields = ['name', 'region', 'district', 'phone', 'address', 'letter_text']
        labels = {
            'name': 'FIO',
            'phone': 'Telefon',
            'address': 'Manzil',
            'letter_text': 'Xat',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'FIO'}),
            'phone': TextInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),
            'address': TextInput(attrs={'placeholder': 'Manzil'}),
        }


class CreateBranchForm(forms.ModelForm):
    name = forms.CharField(label='FIO')
    phone = forms.CharField(label='Telefon')
    region = forms.CharField(label='Viloyat')
    address = forms.CharField(label='Manzil')
    email = forms.CharField(label='Elektron Pochta')
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Parol')

    class Meta:
        model = Staff
        fields = ['name', 'phone', 'region', 'address', 'email', 'username', 'password']
        # labels = {
        #     'name': 'FIO',
        #     'phone': 'Telefon',
        #     'address': 'Manzil',
        #     'letter_text': 'Xat',
        # }
        # widgets = {
        #     'name': TextInput(attrs={'placeholder': 'FIO'}),
        #     'phone': TextInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),
        #     'address': TextInput(attrs={'placeholder': 'Manzil'}),
        # }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Parol'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if not Staff.objects.filter(username=username).exists():
            raise ValidationError('Login xato')
        return username

    def clean_password(self):
        username = self.clean_username()
        password = self.cleaned_data['password']
        user = Staff.objects.filter(username=username).first()
        if not user.check_password(password):
            raise ValidationError('Parol xato')
        return password
