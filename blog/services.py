from django.core.cache import cache

from blog.models import Blog
from config.settings import CACHE_ENABLED


def get_blogs_from_cache():
    """Функция для получения данных о публикациях из кеша"""
    if CACHE_ENABLED:
        key = "blogs_list"
        blogs = cache.get(key)
        if blogs is None:
            blogs = Blog.objects.all()
            cache.set(key, blogs)

    else:
        blogs = Blog.objects.all()

    return blogs
