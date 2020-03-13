import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    query = urllib.parse.parse_qs(environ['QUERY_STRING'])
    username = query['username'][0] if 'username' in query else None
    password = query['password'][0] if 'password' in query else None
    if path == "/register" and username and password:
        product_cursor = cursor.execute('SELECT username FROM users WHERE username = ?', [username])
        product_list = product_cursor.fetchall()
        print(product_list)
        if product_list:
            start_response('200 OK', headers)
            return [("Sorry, username " + username + " is taken.").encode()]
        else:
            connection.execute('INSERT INTO users VALUES (?, ?)', [username, password])
            connection.commit()
            if 'HTTP_COOKIE' in environ:
                start_response('200 OK', headers)
                return[("User " + username + " was successfully registered.").encode()]
    elif path == "/login" and username and password:
        product_cursor = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [username, password])
        product_list = product_cursor.fetchall()
        if product_list:
            headers.append(('Set-Cookie', 'session=' + username + ':' + password))
            start_response('200 OK', headers)
            return[("User " + username + " successfully logged in.").encode()]
        else:
            start_response('200 OK', headers)
            return [("Incorrect username or password.").encode()]
    elif path == "/logout":
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return[("Logged out").encode()]
    elif path == "/account":
        if 'HTTP_COOKIE' in environ:
            cookies = http.cookies.SimpleCookie()
            cookies.load(environ['HTTP_COOKIE'])
            if 'session' in cookies:
                start_response('200 OK', headers)
                return[("You are logged in").encode()]
            else:
                start_response('200 OK', headers)
                return [("You are not logged in").encode()]
        else:
            start_response('200 OK', headers)
            return [("You are not logged in").encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()