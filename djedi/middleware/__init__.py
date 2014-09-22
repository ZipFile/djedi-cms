import cio
from cio.pipeline import pipeline
from django.utils import translation


class DjediCommonMiddleware(object):

    def process_request(self, request):
        # Bootstrap content-io
        pipeline.clear()
        cio.env.reset()

    def process_response(self, request, response):
        pipeline.clear()
        return response

    def process_exception(self, request, exception):
        pipeline.clear()


class DjediTranslationMiddleware(object):

    pushed = False

    def _pop(self):
        if not self.pushed:
            return

        cio.env.pop()
        self.pushed = False

    def _push(self):
        if self.pushed:
            return

        language = translation.get_language()
        cio.env.push_state(i18n=language)
        self.pushed = True

    def process_request(self, request):
        self._push()

    def process_response(self, request, response):
        self._pop()
        return response

    def process_exception(self, request, exception):
        self._pop()
