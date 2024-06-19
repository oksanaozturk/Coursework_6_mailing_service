from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from blog.models import Blog
from main.forms import ClientForm, MessageForm, NewsletterForm
from main.models import Client, Log, Message, Newsletter


class NewsletterListView(ListView):
    """Класс для отображения всех рассылок"""

    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    """Класс для вывода страницы с одной рассылкой по pk"""

    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("main:newsletter_list")

    def form_valid(self, form):
        """Метод для автоматического привязывания Пользователя к создаваемой Рассылке"""
        # Сохранение формы
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования рассылки"""

    model = Newsletter
    form_class = NewsletterForm

    def get_success_url(self):
        """Метод для определения пути, куда будет совершен переход после редактирования рассылки"""
        return reverse("main:newsletter_detail", args=[self.get_object().pk])

    def get_form_class(self):
        """
        Метод, который позволяет вывести Пользователю правильную форму для редактирования,
        в зависимости от прав доступа Пользователя.
        """
        user = self.request.user
        if user == self.object.author or self.request.user.is_superuser:
            return NewsletterForm

        raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления рассылки"""

    model = Newsletter
    success_url = reverse_lazy("main:newsletter_list")


class MessageListView(ListView):
    """Класс для отображения всех созданных сообщений"""

    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Класс для вывода страницы с одним сообщением по pk"""

    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания нового сообщения"""

    model = Message
    form_class = MessageForm

    success_url = reverse_lazy("main:message_list")

    def form_valid(self, form):
        """
        Метод для автоматического привязывания Пользователя к создаваемому Сообщению
        """
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования сообщения"""

    model = Message
    form_class = MessageForm

    def get_success_url(self):
        """Метод для определения пути, куда будет совершен переход после редактирования сообщения"""
        return reverse("main:message_detail", args=[self.get_object().pk])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления сообщения"""

    model = Message
    success_url = reverse_lazy("main:message_list")


class ClientListView(ListView):
    """Класс для отображения всех созданных Клиентов"""

    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Класс для вывода страницы с одним Клиентом по pk"""

    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания нового Клиент"""

    model = Client
    form_class = ClientForm

    success_url = reverse_lazy("main:client_list")

    def form_valid(self, form):
        """
        Метод для автоматического привязывания Пользователя к создаваемому Клиенту
        """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования Клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        """Метод для определения пути, куда будет совершен переход после редактирования сообщения"""
        return reverse("main:client_detail", args=[self.get_object().pk])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления Клиента"""

    model = Client
    success_url = reverse_lazy("main:client_list")


class IndexView(TemplateView):
    """
    Класс для отображения главной страницы с показателями статистики по сайту.
    """

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        """
        Метод получения данных для отображения в виде статистики на Главной странице Проекта.
        """
        context = super().get_context_data(**kwargs)
        article_list = Blog.objects.all()[:3]
        context["article_list"] = article_list
        newsletter_count = Newsletter.objects.all().count()
        context["newsletter_count"] = newsletter_count

        unique_clients_count = Client.objects.all().values("email").distinct().count()
        context["unique_clients_count"] = unique_clients_count

        active_newsletter_count = Newsletter.objects.filter(is_active=True).count()
        context["active_newsletter_count"] = active_newsletter_count
        return context


class LogListView(ListView):
    """
    Класс для отображения всех созданных Логов.
    """

    model = Log

    def get_queryset(self, *args, **kwargs):
        """
        Метод для вывода листа с Логами только для Автора рассылок, при отправке которых эти Логи сформированы.
        """
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = super().get_queryset(*args, **kwargs)
        else:
            queryset = super().get_queryset().filter(owner=user)
        return queryset


def toggle_activity(request, pk):
    """
    Функция для Модератора по смене активности рассылки.
    """
    newsletter_status = get_object_or_404(Newsletter, pk=pk)
    if newsletter_status.is_active is True:
        newsletter_status.is_active = False

    elif newsletter_status.is_active is False:
        newsletter_status.is_active = True

    newsletter_status.save()
    return redirect(reverse("main:newsletter_list"))
