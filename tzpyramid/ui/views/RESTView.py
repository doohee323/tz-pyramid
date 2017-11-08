from tzpyramid.ui.views.get import Get
from pyramid.view import view_defaults
from pyramid.response import Response
from pyramid.view import view_config

@view_defaults(route_name='rest')
class RESTView(object):
    def __init__(self, request):
        self.request = request
    
    def get(self):
        return Response('get')

    def post(self):
        return Response('post')

    def delete(self):
        return Response('delete')

