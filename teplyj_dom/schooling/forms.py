from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import SendQuestion


class SendQuestionForm(forms.ModelForm):
    """Форма для отправки обращения в организацию."""
    hidden_field = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )
    reCAPTCHA = ReCaptchaField(
        label='',
        widget=ReCaptchaV2Checkbox(attrs={
            'data-size': 'normal',
        })
    )

    class Meta:
        model = SendQuestion
        fields = (
            'name', 'phone', 'email', 'subject',
            'text', 'hidden_field',
        )
        labels = {
            'name': _(''),
            'phone': _(''),
            'email': _(''),
            'subject': _(''),
            'text': _(''),
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
                'placeholder': 'Тема обращения',
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Что вас интересует?*',
            }),
        }

        def save(self, commit=True):
            self.cleaned_data.pop('reCAPTCHA', None)
            return super().save(commit=commit)
