from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class SendQuestion(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )
    phone = PhoneNumberField()
    subject = models.CharField(
        max_length=255,
        verbose_name='Тема',
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
    )
    text = models.TextField(
        verbose_name='Текст обращения'
    )

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'Обращение пользователя под номером №{self.id}'


class Project(models.Model):
    start_date = models.DateField(
        verbose_name='Дата начала проекта',
        help_text='Вводить в формате день.месяц.год',
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата окончания проекта',
        help_text='Не обязательное поле. Вводить в формате день.месяц.год',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        help_text='Небольшое количество текста.',
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Основной текст с полным описанием.',
    )
    image = models.ImageField(
        upload_to='project_images',
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект №{self.id}'
