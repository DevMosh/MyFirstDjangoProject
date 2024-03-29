from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

# from trains.forms import TrainForm
from trains.models import Train

__all__ = [
    'home', 'TrainListView',
    'TrainDetailView',
    # 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView',
]


def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get("page")
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    paginate_by = 10
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'


# class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     login_url = '/login/'
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/update.html'
#     success_url = reverse_lazy('train:home')
#     success_message = 'Поезд успешно отредактирован!'
#
#
# class TrainDeleteView(LoginRequiredMixin, DeleteView):
#     login_url = '/login/'
#     model = Train
#     # template_name = 'trains/delete.html'
#     success_url = reverse_lazy('train:home')
#
#     def get(self, request, *args, **kwargs):
#         messages.success(request, 'Поезд успешно удален!')
#         return self.post(request, *args, **kwargs)
