def http_get(host, page):
    import socket
    request = 'GET ' + page + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'
    sock = socket.create_connection((host, 80))
    sock.sendall(request.encode(encoding='utf-8'))
    data = sock.recv(1000)
    sock.close()
    print(data.decode(encoding='utf-8'))
http_get('indstudy1.org', '/CScourses/03b2_minimal-meta.html')