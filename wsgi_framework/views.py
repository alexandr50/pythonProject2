

class BaseView:
    return_code = None
    body = None

    def __call__(self, request):
        return self.return_code, self.body

class NotFoundView:
    return_code = 'Not Found 404'
    body = [b'<h1>Not Found View</h1>']