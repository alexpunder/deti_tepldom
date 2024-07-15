from django.db import models


class AboutItem(models.Model):
    indicator = models.TextField(
        verbose_name='Индикатор',
        help_text='Вторая колонка таблицы на странице "О Нас".',
    )
    info = models.TextField(
        verbose_name='Информация',
        help_text='Третья колонка таблицы на странице "О Нас".',
    )

    class Meta:
        verbose_name = 'Данные страницы "О Нас"'
        verbose_name_plural = 'Данные страницы "О Нас"'

    def __str__(self):
        return f'Запись в таблице №{self.id}'


class OurTeam(models.Model):
    position = models.CharField(
        max_length=255,
        verbose_name='Должность',
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО сотрудника',
        help_text='Вводить через пробел с большой буквы.',
    )
    qualification = models.CharField(
        max_length=255,
        verbose_name='Образование / Квалификация',
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name='Стаж работы',
        help_text='Год начала работы в социальной сфере.',
    )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.full_name
