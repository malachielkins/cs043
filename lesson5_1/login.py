import wsgiref.simple_server
import urllib.parse
import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    query = urllib.parse.parse_qs(environ['QUERY_STRING'])
    print(query)
    username = query['username'][0]
    password = query['password'][0]
    if path == "/register":
        product_cursor = cursor.execute('SELECT username FROM users WHERE username = ?', [username])
        product_list = product_cursor.fetchall()
        print(product_list)
        if product_list:
            start_response('200 OK', headers)
            return [("Sorry, username " + username + " is taken.").encode()]
        else:
            connection.execute('INSERT INTO users VALUES (?, ?)', [username, password])
            connection.commit()
            start_response('200 OK', headers)
            return[("User " + username + " was successfully registered.").encode()]
    if path == "/login":
        product_cursor = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [username, password])
        product_list = product_cursor.fetchall()
        if product_list:
            start_response('200 OK', headers)
            return[("User " + username + " successfully logged in.").encode()]
        else:
            start_response('200 OK', headers)
            return [("Incorrect username or password.").encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()