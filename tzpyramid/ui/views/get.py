from abc import ABC, abstractmethod
from tzpyramid.ui.views import ResourceView


class Get(ABC, ResourceView):
    
    @abstractmethod
    def get(self, request):
        pass
