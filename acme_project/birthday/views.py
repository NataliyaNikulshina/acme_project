from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
# Импортируем модель дней рождения.
from .models import Birthday


def birthday(request):
    print(request.GET)
    # if request.GET:
    #     # ...передаём параметры запроса в конструктор класса формы.
    #     form = BirthdayForm(request.GET)
    #     # Если данные валидны...
    #     if form.is_valid():
    #         # ...то считаем, сколько дней осталось до дня рождения.
    #         # Пока функции для подсчёта дней нет — поставим pass:
    #         pass
    # # Если нет параметров GET-запроса.
    # else:
    #     # То просто создаём пустую форму.
    #     form = BirthdayForm()
    form = BirthdayForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    # Указываем нужный шаблон и передаём в него словарь контекста.
    return render(request, 'birthday/birthday.html', context)


def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context) 