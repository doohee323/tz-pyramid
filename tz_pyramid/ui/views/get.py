from abc import ABC, abstractmethod
from tz_pyramid.ui.views import ResourceView


class Get(ABC, ResourceView):
    
    @abstractmethod
    def get(self, request):
        pass
