from django.urls import path

from cities.views import *

urlpatterns = [
    path("", home, name="home"),
    path("detail/<int:pk>/", CityDetailView.as_view(), name="detail"),  # это нужно для обработки ссылки в которой будет меняться айди
]