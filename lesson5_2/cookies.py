import wsgiref.simple_server
import http.cookies


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8'),
               ('Set-Cookie', 'favoriteColor=green'),
               ('Set-Cookie', 'favoriteNumber=79'),
               ('Set-Cookie', 'name=Malachi')]
    start_response('200 OK', headers)
    print(environ)
    if 'HTTP_COOKIE' in environ:
        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        text = ''
        for key in cookies:
            text += (key + ': ' + cookies[key].value)
        return[text.encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)

print("Serving on port 8000...")

httpd.serve_forever()
