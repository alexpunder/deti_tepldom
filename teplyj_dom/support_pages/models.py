from django.db import models
from django_prose_editor.fields import ProseEditorField


class AboutItem(models.Model):
    indicator = ProseEditorField(
        verbose_name='Индикатор',
        help_text='Вторая колонка таблицы на странице "О Нас".',
    )
    info = ProseEditorField(
        verbose_name='Информация',
        help_text='Третья колонка таблицы на странице "О Нас".',
    )

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return f'Запись в таблице №{self.id}'


class Charity(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name='Полное наименование банка',
        help_text=(
            'Фирменное (полное официальное) наименование '
            'банка на русском языке.'
        ),
    )
    short_name = models.CharField(
        max_length=255,
        verbose_name='Сокращенное наименование банка',
        help_text=(
            'Сокращенное фирменное наименование '
            'банка на русском языке.'
        ),
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Юридический адрес',
    )
    mail_address = models.CharField(
        max_length=255,
        verbose_name='Почтовый адрес',
    )
    correspondent = models.CharField(
        max_length=255,
        verbose_name='Корр. счет',
    )
    checking = models.CharField(
        max_length=255,
        verbose_name='Расчетный счет',
    )
    bik = models.CharField(
        max_length=255,
        verbose_name='БИК',
    )
    inn = models.CharField(
        max_length=255,
        verbose_name='ИНН / КПП',
    )

    class Meta:
        verbose_name = 'Реквизиты поддержки'
        verbose_name_plural = 'Реквизиты поддержки'

    def __str__(self):
        return self.short_name


class Document(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    link = models.URLField(
        verbose_name='Ссылка на документ',
    )

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name


class MassMedia(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    link = models.URLField(
        verbose_name='Ссылка на ресурс',
    )

    class Meta:
        verbose_name = 'СМИ'
        verbose_name_plural = 'СМИ'

    def __str__(self):
        return self.name


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
        ordering = ['id']

    def __str__(self):
        return self.full_name


class UsefullLink(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название',
    )
    link = models.URLField(
        unique=True,
        verbose_name='Ссылка на ресурс',
    )

    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'

    def __str__(self):
        return self.name


class Question(models.Model):
    que = models.CharField(
        max_length=255,
        verbose_name='Вопрос',
    )
    answ = ProseEditorField(
        verbose_name='Ответ',
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.que
