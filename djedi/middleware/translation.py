import cio
from django.utils import translation


class DjediTranslationMiddleware(object):

    def process_request(self, request):
        language = translation.get_language()
        cio.env.push_state(i18n=language)
