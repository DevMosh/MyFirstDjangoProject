from django.db import models


class City(models.Model):  # класс для создания таблице в базе данных
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')  # добавляем ячейку name в таблицу

    def __str__(self):  # для нормального отображения данных в админке
        return self.name

    class Meta:
        verbose_name = 'Город'  # изменяем название ячейки в админке (ед. ч.)
        verbose_name_plural = "Города"  # изменяем название таблицы в админке (мн. ч.)
        ordering = ['name']  # порядок сортировки, чтобы новые элементы шли вниз

