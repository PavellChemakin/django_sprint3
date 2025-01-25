from django.db import models
from django.contrib.auth import get_user_model

from blogicum.settings import MAX_TITLE_LENGTH

User = get_user_model()


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию."
    )

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField(max_length=MAX_TITLE_LENGTH,
                             verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name="Идентификатор",
        help_text="Идентификатор страницы для URL; разрешены "
                  "символы латиницы, цифры, дефис и подчёркивание."
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Добавлено")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title[:15]


class Location(PublishedModel):
    name = models.CharField(max_length=MAX_TITLE_LENGTH,
                            verbose_name="Название места")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Добавлено")

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name[:15]


class Post(PublishedModel):
    title = models.CharField(max_length=MAX_TITLE_LENGTH,
                             verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text="Если установить дату и время в будущем — "
                  "можно делать отложенные публикации."
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True,
        blank=True, verbose_name="Местоположение"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        verbose_name="Категория"
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Добавлено")
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Идентификатор',
        help_text="Идентификатор страницы для URL; разрешены "
                  "символы латиницы, цифры, дефис и подчёркивание.",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title[:15]
