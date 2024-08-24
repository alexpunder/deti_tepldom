import re

from django.core.exceptions import ValidationError

from teplyj_dom.constants import SPAM_PATTERNS_DATA

SPAM_PATTERNS = re.compile(SPAM_PATTERNS_DATA, re.IGNORECASE)
RUSSIAN_ALPH_PATTERN = r'^[А-Яа-яЁё]*$'


def spam_validator(text):
    """Валидатор спам-слов и вредоносных тегов."""
    if SPAM_PATTERNS.search(text):
        raise ValidationError(
            'К сожалению, текст не прошел первичную проверку.'
        )


def username_at_russian_alphabet(name):
    if not re.match(RUSSIAN_ALPH_PATTERN, name):
        raise ValidationError(
            'Допустимы символы только русского алфавита.'
        )
