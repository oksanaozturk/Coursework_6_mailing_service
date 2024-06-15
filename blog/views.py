from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from pytils.translit import slugify

from blog.models import Blog
from blog.services import get_blogs_from_cache


class BlogCreateView(CreateView):
    """Класс для создания нов.публикации"""

    model = Blog
    fields = ("title", "content", "preview", "view_counter")
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        """Метод для динамического формирования slug name для заголовка"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    """Класс лоя просмотра всех публикаций."""

    model = Blog

    def get_queryset(self):
        """Переопределяем работу метода (он получает данные из БД), для функционирования кеша,
        теперь она будет выводить данные, полученные при отработке функции get_blogs_from_cache."""

        queryset = get_blogs_from_cache()
        return queryset


class BlogDetailView(DetailView):
    """Класс для просмотра детальной информации публикации."""

    model = Blog

    def get_object(self, queryset=None):
        """Метод для работы счетчика просмотров публикации"""
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Класс для редактирования публикации"""

    model = Blog
    fields = ("title", "content", "preview", "view_counter")

    def get_success_url(self):
        """Метод для перенаправлять пользователя на просмотр этой статьи после её редактирования"""
        return reverse("blog:view", args=[self.kwargs.get("slug")])


class BlogDeleteView(DeleteView):
    """Класс  для удаления публикации"""

    model = Blog
    success_url = reverse_lazy("blog:list")
