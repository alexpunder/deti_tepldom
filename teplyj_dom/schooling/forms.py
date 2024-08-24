from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import SendQuestion
from .validators import spam_validator, username_at_russian_alphabet


class SendQuestionForm(forms.ModelForm):
    """Форма для отправки обращения в организацию."""

    reCAPTCHA = ReCaptchaField(
        label='',
        widget=ReCaptchaV2Checkbox(attrs={
            'data-size': 'normal',
        })
    )
    nickname = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'style': 'display:none;',
        }),
        required=False,
    )

    def save(self, commit=True):
        self.cleaned_data.pop('reCAPTCHA', None)
        return super().save(commit=commit)

    def clean_name(self):
        data = self.cleaned_data.get('name')
        username_at_russian_alphabet(data)
        return data

    def clean_nickname(self):
        data = self.cleaned_data.get('nickname')
        if data:
            raise forms.ValidationError(
                'Введено недопустимое значение, попробуйте другое.'
            )
        return data

    def clean_subject(self):
        data = self.cleaned_data.get('subject')
        spam_validator(data)
        return data

    def clean_text(self):
        data = self.cleaned_data.get('text')
        spam_validator(data)
        return data

    class Meta:
        model = SendQuestion
        fields = (
            'name', 'phone', 'email', 'subject', 'text',
        )
        labels = {
            'name': _(''),
            'phone': _(''),
            'email': _(''),
            'subject': _(''),
            'text': _(''),
        }
        help_texts = {
            'text': _('Все поля обязательны к заполнению.')
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя*',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Телефон*',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Электронная почта*',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Тема обращения*',
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Что вас интересует?*',
            }),
        }
