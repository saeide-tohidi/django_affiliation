from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)
AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    return "".join([choice(chars) for _ in range(SIZE)])


def create_shortened_url(model):
    random_code = create_random_code()
    model_class = model
    if model_class.objects.filter(slug=random_code).exists():
        return create_shortened_url(model)
    return random_code
