from django import forms
from django.forms import TextInput

from app.models import Region, District, Letter


class CreateLetterForm(forms.ModelForm):
    # name = forms.CharField(label='FIO', widget=forms.TextInput(attrs={'placeholder': 'FIO'}))
    # region = forms.ModelChoiceField(label='Viloyat', queryset=Region.objects.all())
    # district = forms.ModelChoiceField(label='Tuman', queryset=District.objects.all())
    # phone = forms.IntegerField(label='Telefon',
    #                            widget=forms.TextInput(attrs={'placeholder': 'Telefon', 'type': 'number'}))
    # address = forms.CharField(label='Manzil', widget=forms.TextInput(attrs={'placeholder': 'Manzil'}))

    class Meta:
        model = Letter
        fields = ['name', 'region', 'district', 'phone', 'address', 'letter_text']
        labels = {
            'name': 'FIO',
            'region': 'Viloyat',
            'district': 'Tuman',
            'phone': 'Telefon',
            'address': 'Manzil',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'FIO'}),
            'region': TextInput(attrs={'placeholder': 'Viloyat'}),
            'district': TextInput(attrs={'placeholder': 'Tuman'}),
            'phone': TextInput(attrs={'placeholder': 'Telefon', 'type': 'number'}),
            'address': TextInput(attrs={'placeholder': 'Manzil'}),
        }
