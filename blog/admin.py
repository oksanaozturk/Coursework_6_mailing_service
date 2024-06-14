from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Класс для регистрации публикации в админке."""

    list_display = ("id", "title", "date_published", "view_counter", "slug")
    list_filter = ("date_published",)
    search_fields = (
        "title",
        "date_published",
    )
