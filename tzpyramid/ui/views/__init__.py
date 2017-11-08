from pyramid.httpexceptions import HTTPFound, HTTPInternalServerError, HTTPMethodNotAllowed
from pyramid.response import Response
from re import compile


ENABLE_DISABLE = ('enable', 'disable')
UP_DOWN = ('up', 'down')
XSS_VULNERABLE_REGEX = compile('[<>()#"\']')
CFG_OK = 0
SCEP_OK = 0


def active_from_param(params, name):
    return 'active' if params.get(name) else 'inactive'


def enable_from_param(params, name):
    return 'enable' if params.get(name) else 'disable'


def enabled_from_param(params, name):
    return 'enabled' if params.get(name) else 'disabled'


def _flash(request, category, message, queue):
    # TODO: If the 'message' parameter is a list (which is supported), translate each member individually.
    # Otherwise, if it's a string, translate that.
    request.session.flash((category, request.localizer.translate(message)), queue)


def flash_error(request, message, queue='authenticated'):
    _flash(request, 'danger', message, queue)


def flash_success(request, message, queue='authenticated'):
    _flash(request, 'success', message, queue)


def flash_warning(request, message, queue='authenticated'):
    _flash(request, 'warning', message, queue)


def get_child_object_by_key(key, value, elements):
    for e in elements:
        if e[key] == value:
            return e
    return {}


def none_unless_in(v, s):
    if isinstance(s, range):
        try:
            v = int(v)
        except TypeError or ValueError:
            return None
    return v if v in s else None


def none_unless_xss_safe(text, max_length=None):
    return None if ((max_length and len(text) > max_length) or XSS_VULNERABLE_REGEX.match(text)) else text


def raise_unless_in(v, s):
    if isinstance(v, range):
        v = int(v)
    if v in s:
        return v
    else:
        raise ValueError


class ResourceView:

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.methods = [c.__name__.lower() for c in self.__class__.__bases__]

    def __call__(self):
        context = self.context
        request = self.request
        root = request.root
        login = root['login']
        logout = root['logout']

        if context == logout:
            authentication_ticket = None
        else:
            authentication_ticket = request.authenticated_userid
            if context != login and not authentication_ticket:
                request.session['next'] = request.path
                return HTTPFound(request.resource_url(login))

        method = request.method.lower()
        if method not in self.methods:
            return HTTPMethodNotAllowed()

        result = getattr(self, method)(request)
        if isinstance(result, Response):
            return result
        elif isinstance(result, dict):
            data = dict(
                title=context.title,
                username=getattr(authentication_ticket, 'username', None)
            )
            data.update(result)
            return data
        elif result:
            return Response(result)
        else:
            return HTTPInternalServerError()
