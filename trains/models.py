from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


# Create your models here.


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='время в пути')
    # from_city = models.ForeignKey(to=City, on_delete=models.CASCADE)  # ВСЕ ЗАПИСИ, КОТОРЫЕ БЫЛИ ПРИВЯЗАНЫ К СИТИ БУДУТ УДАЛЕНЫ, ЕСЛИ УДАЛИЛАС ЗАПИСЬ В СИТИ
    # from_city = models.ForeignKey(to=City, on_delete=models.PROTECT)  # ЕСЛИ ЭТА ЗАПИСЬ ПРИВЯЗАНА К КАКОМУ-ТО ГОРОДУ, ТО ГОРОД НЕЛЬЗЯ БУДЕТ УДАЛИТЬ
    # from_city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True, blank=True)  # ВСЕ ЗАПИСИ, КОТОРЫЕ БЫЛИ ПРИВЯЗАНЫ К СИТИ ОТВЯЖУТСЯ И НЕ УДАЛЯТСЯ
    from_city = models.ForeignKey(to=City, on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='Из какого города')

    to_city = models.ForeignKey(to='cities.City', on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='В какого города')

    def __str__(self):  # для нормального отображения данных в админке
        return f'Поезд №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Поезд'  # изменяем название ячейки в админке (ед. ч.)
        verbose_name_plural = "Поезда"  # изменяем название таблицы в админке (мн. ч.)
        ordering = ['travel_time']  # порядок сортировки, чтобы новые элементы шли вниз

    def clean(self):  # делаем предварительную проверку тех данных, которые мы собираемся сохранить

        # проверяем, чтобы город не вышел и не зашел в себя
        if self.from_city == self.to_city:
            raise ValidationError('Измените город прибытия или отправления.')

        # если есть хотяб одна запись с таким же временем и с одинаковыми городами
        qs = Train.objects.filter(from_city=self.from_city,
                                  to_city=self.to_city,
                                  travel_time=self.travel_time).exclude(pk=self.pk)
        # Train == self.__class__ ( потому что мы находимся в этом же классе )
        if qs.exists():
            raise ValidationError('Измените время в пути')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



# class TrainTest(models.Model):
#     name = models.CharField(max_length=50, unique=True,
#                             verbose_name='Номер поезда')
#     # from_city = models.ForeignKey(to=City, on_delete=models.CASCADE)  # ВСЕ ЗАПИСИ, КОТОРЫЕ БЫЛИ ПРИВЯЗАНЫ К СИТИ БУДУТ УДАЛЕНЫ, ЕСЛИ УДАЛИЛАС ЗАПИСЬ В СИТИ
#     # from_city = models.ForeignKey(to=City, on_delete=models.PROTECT)  # ЕСЛИ ЭТА ЗАПИСЬ ПРИВЯЗАНА К КАКОМУ-ТО ГОРОДУ, ТО ГОРОД НЕЛЬЗЯ БУДЕТ УДАЛИТЬ
#     # from_city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True, blank=True)  # ВСЕ ЗАПИСИ, КОТОРЫЕ БЫЛИ ПРИВЯЗАНЫ К СИТИ ОТВЯЖУТСЯ И НЕ УДАЛЯТСЯ
#     from_city = models.ForeignKey(to=City, on_delete=models.CASCADE,
#                                   related_name='from_city',
#                                   verbose_name='Из какого города')