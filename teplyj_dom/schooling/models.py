from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django_prose_editor.fields import ProseEditorField


class SendQuestion(models.Model):
    is_complete = models.CharField(
        max_length=255,
        default='Нет',
        choices=(('Да', 'Да'), ('Нет', 'Нет')),
        verbose_name='Обработан?',
        help_text='Если заявка обработа, выберите "Да".',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )
    phone = PhoneNumberField(
        verbose_name='Телефон',
    )
    subject = models.CharField(
        max_length=255,
        default='',
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
    short_description = ProseEditorField(
        verbose_name='Краткое описание',
        help_text='Основные тезисы проекта, цели и краткая информация.',
    )
    text = ProseEditorField(
        verbose_name='Текст',
        help_text='Основной текст с полным описанием.',
    )
    main_image = models.ImageField(
        upload_to='main_projects_images',
        verbose_name='Титульное изображение',
        help_text='Изображение-обложка для страницы проекта.',
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект №{self.id}'


class ProjectImage(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.SET_NULL,
        null=True,
        related_name='images',
        verbose_name='Проект',
    )
    image = models.ImageField(
        upload_to='project_images',
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Изображения проекта'
        verbose_name_plural = 'Изображения проектов'

    def __str__(self):
        return f'Изображение проекта №{self.id}'


class MainGallery(models.Model):
    image = models.ImageField(
        upload_to='main_gallery',
        verbose_name='Изображение на главной',
    )

    class Meta:
        verbose_name = 'Изображение на главной'
        verbose_name_plural = 'Изображения на главной'

    def __str__(self):
        return f'Изображение на главной №{self.id}'
