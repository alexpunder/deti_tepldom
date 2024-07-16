from django.db import models
from django.utils.text import slugify
from django_prose_editor.fields import ProseEditorField


class Blog(models.Model):
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Устанавливается автоматически в момент создания.',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор URL',
        help_text='Автоматически заполняемое поле. Не вносить изменения.',
    )
    text = ProseEditorField(
        verbose_name='Основное содержание',
    )
    main_image = models.ImageField(
        upload_to='main_news_images',
        verbose_name='Титульное изображение',
        help_text='Изображение-обложка для страницы новости.',
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name='Категория',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Тег',
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
