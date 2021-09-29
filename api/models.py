from django.db import models


class User(models.Model):
    salary = models.PositiveIntegerField(verbose_name='Зарплата')
    name = models.CharField(max_length=50,
                            verbose_name='Имя')
    date = models.DateTimeField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'

    def __str__(self):
        return f'{self.name} - {self.salary}'


class House(models.Model):
    owner = models.ForeignKey('User',
                              on_delete=models.CASCADE,
                              related_name='houses',
                              verbose_name='Пользователь')
    address = models.TextField(max_length=150,
                               verbose_name='Адрес')
    cost = models.PositiveIntegerField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Список недвижимости'

    def __str__(self):
        return f'{self.owner} - {self.address}'
