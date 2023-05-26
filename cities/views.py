from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import CityForm
from cities.models import City

__all__ = [
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView',
    'CityListView',
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

    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get("page")
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context['hello'] = 'hello world'
        return context

    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно создан'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'город успешно отредактирован'


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'  # это типо способ с подтверждением удаления
    success_url = reverse_lazy('cities:home')

    # способ без подтверждения удаления:
    def get(self, request, *args, **kwargs):
        messages.success(request, 'город успешно удален')
        return self.delete(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 10
    model = City
    template_name = 'cities/home.html'

    # функция, которая отобразит форму добавления города
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context
