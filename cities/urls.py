from django.urls import path

from cities.views import *

urlpatterns = [
    # path("", home, name="home"),
    path("", CityListView.as_view(), name="home"),
    path("detail/<int:pk>/", CityDetailView.as_view(), name="detail"),  # это нужно для обработки ссылки в которой будет меняться айди
    path("update/<int:pk>/", CityUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", CityDeleteView.as_view(), name="delete"),
    path("add/", CityCreateView.as_view(), name="create"),  # это нужно для обработки ссылки в которой будет меняться айди
]