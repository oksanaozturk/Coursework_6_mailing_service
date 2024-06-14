from django.forms import BooleanField, DateTimeInput, ModelForm

from main.models import Client, Message, Newsletter


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
        exclude = ("datetime_send", "author")

        widgets = {
            "datetime_start": DateTimeInput(
                attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС", "type": "datetime-local"}
            ),
            "datetime_finish": DateTimeInput(
                attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС", "type": "datetime-local"}
            ),
        }


class MessageForm(StyleFormMixin, ModelForm):
    """Класс создания форм для модели Message"""

    class Meta:
        model = Message
        fields = ("subject", "body")


class ClientForm(StyleFormMixin, ModelForm):
    """Класс создания форм для модели Client"""

    class Meta:
        model = Client
        fields = ("email", "name")
