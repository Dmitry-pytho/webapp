from django.db import models

from random import randrange


class Filters(models.Model):
    MATERIAL_CHOICES = [
        ('PP', 'PP'),
        ('GF', 'GF'),
        ('SM', 'SM')
    ]

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'

    filter_type = models.CharField('Тип фильтра (рабочая среда)', max_length=15)
    external_diam = models.CharField('Наружный диаметр, мм', choices=[(x, x) for x in range(1, 300)], default='10',
                                     max_length=3)
    internal_diam = models.CharField('Внутренний диаметр, мм', choices=[(x, x) for x in range(1, 300)], default='10',
                                     max_length=3)
    length = models.CharField('Длина, мм', choices=[(x, x) for x in range(1, 1000)], default='10', max_length=4)
    filter_material = models.CharField('Фильтрующий материал', choices=MATERIAL_CHOICES, default='GF', max_length=15)
    thickness = models.CharField('Тонкость фильтрации, мкм', choices=[(x, x) for x in range(5, 105,5)], max_length=4)
    pressure = models.CharField('Давление', max_length=4)
    end_filter = models.CharField('Тип торца', max_length=10)

    def __str__(self):
        return self.filter_type
