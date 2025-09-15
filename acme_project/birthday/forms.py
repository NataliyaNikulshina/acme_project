# birthday/forms.py
from django import forms

from .models import Birthday
from django.core.exceptions import ValidationError

# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(required=False)
    # birthday = forms.DateField()
    # first_name = forms.CharField(label='Имя', max_length=20)
    # last_name = forms.CharField(
    #     label='Фамилия', required=False, help_text='Необязательное поле'
    # )
    # birthday = forms.DateField(
    #     label='Дата рождения',
    #     # Указываем, что виджет для ввода даты должен быть с типом date.
    #     widget=forms.DateInput(attrs={'type': 'date'})
    # )
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'ГГГГ-ММ-ДД'},
                format='%Y-%m-%d'        # формат вывода в input
            ),
        }

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        super().clean()
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз,'
                'но введите, пожалуйста, настоящее имя!'
            )
