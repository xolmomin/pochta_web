from django.forms import CheckboxSelectMultiple
from django_filters import FilterSet, CharFilter, ChoiceFilter, ModelMultipleChoiceFilter, ModelChoiceFilter

from app.models import Letter


class LetterFilter(FilterSet):
    # region = ChoiceFilter(label='Viloyat')
    # district = ModelChoiceFilter(label='Tuman', field_name='region_name', queryset=Letter.objects.all())

    class Meta:
        model = Letter
        fields = ('region', 'district')
        labels = {
            'region': 'Viloyat',
            'district': 'Tuman',
        }
