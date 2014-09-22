import cio
from django.utils import translation
from . import DjediMiddleware


# FIXME: Do not inherit DjediMiddleware
class DjediTranslationMiddleware(DjediMiddleware):

    def process_request(self, request):
        super(DjediTranslationMiddleware, self).process_request(request)
        language = translation.get_language()
        cio.env.push_state(i18n=language)
