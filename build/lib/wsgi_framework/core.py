from .views import NotFoundView
from .middleware import MobileRefererMiddleware

class Application:
    urls = None
    middlewares = [
        MobileRefererMiddleware()
    ]

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswoth('/'):
            path += '/'

        view = self.urls.get(path, NotFoundView())
        request = {}

        for middleware in self.middlewares:
            middleware(environ, request)

        code, body = view(request)

        start_response('code', [('Content-type', 'text/html')])
        return body