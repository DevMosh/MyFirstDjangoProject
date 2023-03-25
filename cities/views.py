from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = [
    'home', 'CityDetailView'
]


def home(request, pk=None):
    """эта функция обрабатывает страницу при переходе по сссылке,
    у которой меняется айди ( в данном случае она позволяет посмотреть
    больше информации о городе )"""

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():  # это условие будет проверять все ли введеные поля соответсвуют заявленным в нашей форме, которая находится в файле forms.py
            print(form.cleaned_data)
            form.save()

    # if pk:
        # city = City.objects.filter(id=pk).first()  # чтобы ничего не вышло
        # city = get_object_or_404(City, id=pk)  # чтобы вышла ошибка 404, которая означает что страница не существует
        # context = {'object': 8}
        # try:
        #     city = City.objects.get(pk=pk)  # в этом случае будет ошибка, но ее можно самостоятельно обработать
        #     context = {'object': city.name}
        # except City.DoesNotExist:
        #     context = {'object': "Такого города нет в базе данных."}
        # return render(request, 'cities/detail.html', context)

    form = HtmlForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


