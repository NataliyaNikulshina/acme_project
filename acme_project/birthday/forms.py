# birthday/forms.py
from django import forms

from .models import Birthday


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
