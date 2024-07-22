from django import forms
from django.utils.translation import gettext_lazy as _

from .models import SendQuestion


class SendQuestionForm(forms.ModelForm):
    """Форма для отправки обращения в организацию."""

    class Meta:
        model = SendQuestion
        exclude = ('id', 'is_complete', 'datetime_to')
        labels = {
            'name': _(''),
            'phone': _(''),
            'email': _(''),
            'subject': _(''),
            'text': _(''),
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Телефон'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Электронная почта'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Тема обращения'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Что вас интересует?'
            }),
        }
