from django.forms import ModelForm

from .models import MainPersonData


class MainDataForm(ModelForm):
    class Meta:
        model = MainPersonData
        fields = ['name', 'age', 'sex', 'height', 'weight', 'smoking']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        age = cleaned_data.get('age')
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        if len(name) < 1:
            self.add_error('name', 'Имя не может состоять из одной буквы')
        if age < 21:
            self.add_error('age', 'Возраст должен быть больше 20')
        if height <= 0:
            self.add_error('height', 'Рост не может быть равен нулю')
        if weight <= 0:
            self.add_error('weight', 'Вес не может быть равен нулю')
        return cleaned_data
