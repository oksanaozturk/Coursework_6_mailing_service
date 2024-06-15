from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import (ClientCreateView, ClientDeleteView, ClientDetailView,
                        ClientListView, ClientUpdateView, IndexView,
                        LogListView, MessageCreateView, MessageDeleteView,
                        MessageDetailView, MessageListView, MessageUpdateView,
                        NewsletterCreateView, NewsletterDeleteView,
                        NewsletterDetailView, NewsletterListView,
                        NewsletterUpdateView, toggle_activity)

app_name = MainConfig.name

urlpatterns = [
    # Путь для отображения главной страницы
    path("", cache_page(60)(IndexView.as_view()), name="index"),
    # Путь для вывода листа со всеми рассылками
    path("newsletters/", NewsletterListView.as_view(), name="newsletter_list"),
    # Путь для вывода листа с одной рассылкой
    path(
        "newsletters/<int:pk>/",
        NewsletterDetailView.as_view(),
        name="newsletter_detail",
    ),
    # Путь для создания нового объекта модели Newsletter
    path(
        "newsletters/create/", NewsletterCreateView.as_view(), name="newsletter_create"
    ),
    # Путь для редактирования рассылки
    path(
        "newsletters/<int:pk>/update/",
        NewsletterUpdateView.as_view(),
        name="newsletter_update",
    ),
    # Путь для удаления рассылки
    path(
        "newsletters/<int:pk>/delete/",
        NewsletterDeleteView.as_view(),
        name="newsletter_delete",
    ),
    # Путь для вывода листа со всеми cсообщениями
    path("messages/", MessageListView.as_view(), name="message_list"),
    # Путь для вывода листа с одном сообщением
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    # Путь для создания нового объекта модели Message
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    # Путь для редактирования сообщения
    path(
        "messages/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"
    ),
    # Путь для удаления сообщения
    path(
        "messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"
    ),
    # Путь для вывода листа со всеми Клиентами
    path("clients/", ClientListView.as_view(), name="client_list"),
    # Путь для вывода листа с одном Клиентом
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    # Путь для создания нового объекта модели Client
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),
    # Путь для редактирования Клиента
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    # Путь для удаления Клиента
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    # Путь для вывода листа с Логами
    path("logs/", LogListView.as_view(), name="logs_list"),

    path("activity/<int:pk>/", toggle_activity, name="toggle_activity"),
]
