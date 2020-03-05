from django.forms import ModelForm

from .models import MainPersonData


class MainDataForm(ModelForm):
    class Meta:
        model = MainPersonData
        fields = ['name', 'age', 'sex', 'height', 'weight']
