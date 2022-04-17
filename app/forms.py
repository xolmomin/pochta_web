from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import TextInput

from app.models import Region, District, Letter


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
