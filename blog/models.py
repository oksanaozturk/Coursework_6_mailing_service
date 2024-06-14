from django.db import models

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    """Класс для создания модели блоговой записи"""

    title = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите название статьи"
    )
    content = models.TextField(
        verbose_name="Содержимое", **NULLABLE, help_text="Добавьте содержимое"
    )
    preview = models.ImageField(
        upload_to="blog_foto",
        verbose_name="Изображение",
        **NULLABLE,
        help_text="Добавьте изображение"
    )
    date_published = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    view_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = (
            "title",
            "date_published",
            "view_counter",
        )

    def __str__(self):
        return self.title
