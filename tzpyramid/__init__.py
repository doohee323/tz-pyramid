from pyramid.config import Configurator
from pyramid.config import not_
from tzpyramid.ui.views.RESTView import *

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('home2', '/home2')
    config.add_view(
        'tzpyramid.views.my_view',
        request_method=not_('GET,HEAD'),
        route_name='home2',
        renderer='templates/mytemplate2.jinja2'
        )
    
    config.add_route('rest', '/rest')
    config.add_view(RESTView, attr='get', request_method='GET', http_cache=3600)
    config.add_view(RESTView, attr='post', request_method='POST')
    config.add_view(RESTView, attr='delete', request_method='DELETE')
    
    config.scan()
    return config.make_wsgi_app()
