from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Класс для создание модели клиента"""

    email = models.EmailField(verbose_name="email", help_text='Введите Вашу электронную почту')
    name = models.CharField(max_length=200, verbose_name='ФИО', help_text='Введите Ваши ФИО')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True,)
    owner = models.ForeignKey(User, verbose_name='Пользователь', related_name="clients", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"Клмент сервиса: {self.name}, email: {self.email}"


class Message(models.Model):
    """Класс для создания модели Сообщения рассылки"""

    subject = models.CharField(max_length=200, verbose_name="тема письма", help_text="Укажите тему сообщения")
    body = models.TextField(verbose_name="Тело письма", help_text="Заполните тело сообщения")
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, related_name="messages")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Заголовок сообщения: {self.subject}"


class Newsletter(models.Model):
    """Класс для создания модели Рассылки"""

    CHOICES_PERIOD = [
        ("daily", "раз в день"),
        ("weekly", "раз в неделю"),
        ("monthly", "раз в месяц"),
    ]

    STATUS_CHOICES = [
        ("completed", "Завершена"),
        ("created", "Создана"),
        ("launched", "Запущена"),
    ]

    title = models.CharField(max_length=200, verbose_name=" Название рассылки", help_text="Напишите название рассылки")
    author = models.ForeignKey(User, verbose_name="Автор рассылки", related_name="newsletters",
                               on_delete=models.CASCADE)
    message = models.ForeignKey(Message, verbose_name="Сообщение рассылки", on_delete=models.CASCADE)
    date_start = models.DateTimeField(default=timezone.now, verbose_name="Дата начала")
    date_next = models.DateTimeField(default=timezone.now, verbose_name="Дата следующей отправки")
    date_finish = models.DateTimeField(default=timezone.now, verbose_name="Дата окончания")
    periodicity = models.CharField(max_length=50, choices=CHOICES_PERIOD,
                                   verbose_name="Периодичность")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="created", verbose_name="Статус рассылки")
    clients = models.ManyToManyField(Client, verbose_name="Получатели рассылки")
    is_active = models.BooleanField(default=True, verbose_name="Актуальность")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return (f" Рассылка {self.title}, дата начала: {self.date_start}, дата окончания: {self.date_finish}, "
                f"периодичность: {self.periodicity} ")


class Log(models.Model):
    """Класс для создания модели Сообщения"""

    newsletter = models.ForeignKey(Newsletter, verbose_name="Рассылка", on_delete=models.CASCADE, related_name="logs")
    last_time_send = models.DateTimeField(auto_now=True, verbose_name="Дата и время последней попытки")
    status = models.CharField(max_length=50, verbose_name="Статус попытки")
    server_response = models.TextField(verbose_name="Ответ сервера", **NULLABLE)

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"

    def __str__(self):
        return f"Дата и время последней попытки: {self.last_time_send}, статус попытки: {self.status}"