from django.db import models


class Filters(models.Model):
    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'

    TYPE_CHOICES = [
        ('Фильтр гидравлический', 'Фильтр гидравлический'),
        ('Фильтр воздушный', 'Фильтр воздушный'),
        ('Фильтр топливный', 'Фильтр топливный'),
        ('Фильтр водяной', 'Фильтр водяной')
    ]
    filter_type = models.CharField('Тип фильтра (рабочая среда)', choices=TYPE_CHOICES, max_length=30)
    external_diam = models.IntegerField('Наружный диаметр, мм', choices=[(x, x) for x in range(1, 300)])
    internal_diam = models.IntegerField('Внутренний диаметр, мм', choices=[(x, x) for x in range(1, 300)])
    length = models.IntegerField('Длина, мм', choices=[(x, x) for x in range(1, 1000)])
    MATERIAL_CHOICES = [
        ('Полипропилен', 'Полипропилен'),
        ('Стекловолокно', 'Стекловолокно'),
        ('Металлическая сетка', 'Металлическая сетка')
    ]
    filter_material = models.CharField('Фильтрующий материал', choices=MATERIAL_CHOICES, max_length=20)
    thickness = models.IntegerField('Тонкость фильтрации, мкм', choices=[(x, x) for x in range(5, 500, 5)])
    PRESSURE_CHOICES = [
        ('Низкоперепадный - 30 бар', 'Низкоперепадный - 30 бар'),
        ('Высокоперепадный -  210 бар', 'Высокоперепадный -  210 бар')
    ]
    pressure = models.CharField('Допустимый перепад давления на фильтре, бар', choices=PRESSURE_CHOICES, max_length=30)
    END_CHOICES = [
        ('Глухой', 'Глухой'),
        ('Сквозной', 'Сквозной'),
        ('С байпасным клапаном', 'С байпасным клапаном')
    ]
    end_filter = models.CharField('Тип торца', choices=END_CHOICES, max_length=20)

    if end_filter == 'С байпасным клапаном':
        bypass_presuure = models.IntegerField('Давление открытия клапана, бар', choices=[(x, x) for x in range(1, 10, 1)])



    SEALS_CHOICES = [
        ('FPM', 'FPM'),
        ('NBR', 'NBR'),
        ('PTFE', 'PTFE'),
        ('Без уплотнений', 'Без уплотнений')
    ]
    seals_type = models.CharField('Материал уплотнений фильтрующего элемента', choices=SEALS_CHOICES, max_length=20)


    def __str__(self):
        return self.filter_type
