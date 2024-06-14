from django.contrib import admin

from main.models import Client, Log, Message, Newsletter


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Клиента в админке."""

    list_display = ("name", "email", "owner")
    list_filter = ("name",)
    search_fields = ("email",)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Рассылки в админке."""

    list_display = (
        "title",
        "author",
        "datetime_start",
        "datetime_send",
        "datetime_finish",
        "periodicity",
        "status",
        "is_active",
    )
    list_filter = ("title",)
    search_fields = ("title", "author")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Сообщения в админке."""

    list_display = ("id", "subject", "body", "author")
    search_fields = ("subject", "author")


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Лога в админке."""

    list_display = ("newsletter", "last_time_send", "status", "server_response")
    search_fields = ("newsletter",)
