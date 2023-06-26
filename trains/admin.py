from django.contrib import admin

from trains.models import Train


# делаем данные в админке более информативными
class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train
    list_display = ('name', 'from_city', 'to_city', 'travel_time')

    # даст возможность редактировать поле с главной страницы
    list_editable = ('travel_time', )  # 'from_city' - изменение таких данных увеличит нагрузку


admin.site.register(Train, TrainAdmin)
