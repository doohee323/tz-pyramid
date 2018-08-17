from abc import ABC, abstractmethod
# noinspection PyPep8Naming
from pyramid.i18n import TranslationString as _
from tz_pyramid.ui.views import ResourceView


def invalid_data_message(field):
    return _('Invalid data received for $field.', mapping={'field': field})


class Post(ABC, ResourceView):

    @abstractmethod
    def post(self, request):
        pass
