from django.forms import ModelForm

from .models import MainPersonData


class MainDataForm(ModelForm):
    class Meta:
        model = MainPersonData
        fields = ['name', 'age', 'sex', 'height', 'weight']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 1:
            raise ValueError('Имя не может состоять из одной буквы')
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 21:
            raise ValueError('Возраст должен быть больше 20')
        return age

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height <= 0:
            raise ValueError('Рост не может быть равен нулю')
        return height

    def clean_weight(self):
        weight = self.cleaned_data('weight')
        if weight <= 0:
            raise ValueError('Вес не может быть равен нулю')
        return weight
