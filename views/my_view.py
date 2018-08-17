# from resources import MyResource
from pyramid.view import view_config
from pyramid.response import Response

# @view_config(route_name='home2', request_method='GET', permission='read')
# @view_config(request_method='GET',
#         route_name='home2',
#         permission='read',
#         renderer='templates/mytemplate2.jinja2')
def my_view(request):
    return {'project': 'tz_pyramid22'}

