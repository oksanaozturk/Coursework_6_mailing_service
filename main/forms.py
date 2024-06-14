from django.forms import ModelForm, BooleanField

from main.models import Newsletter, Message, Client


# Данный класс создаем для стилизации форм, Это Mixin, класс ни от чего не наследуется
class StyleFormMixin:
    """Класс для стилизации форм"""

    # Переопределяем метод __init__
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Так как мы получаем словарь, для выведения обоих значение (value| key) применяем значение items()
        for field_name, field in self.fields.items():
            # Задаем условия - если у поля Булевое значение
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class NewsletterForm(StyleFormMixin, ModelForm):
    """Класс создания форм для модели Newsletter"""

    class Meta:
        model = Newsletter
        fields = "__all__"


class MessageForm(StyleFormMixin, ModelForm):
    """Класс создания форм для модели Message"""

    class Meta:
        model = Message
        fields = ("subject", "body", "author")


class ClientForm(StyleFormMixin, ModelForm):
    """Класс создания форм для модели Client"""

    class Meta:
        model = Client
        fields = ("email", "name", "owner")
