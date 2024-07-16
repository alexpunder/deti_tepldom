from django.forms import ModelForm

from .models import SendQuestion


class SendQuestionForm(ModelForm):

    class Meta:
        model = SendQuestion
        exclude = ('id', 'is_complete',)
