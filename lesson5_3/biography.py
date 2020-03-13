import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response('200 OK', headers)

    path = environ['PATH_INFO']
    if path == '/biography':
        page = '''<!DOCTYPE html>
        <html><head><title>Biography</title></head><body>
        <h1>Hi, I'm Barry Scott</h1>
        <h2 style="background-color: lightblue">My Famous Speech</h2>
        <div>"Bang and the cold is gone!"</div>
        <h2 style="background-color: green">What I Like</h2>
        <p>I like feet</p>
        <p style="color: red">"But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."</p>
        <p>Barry Scott's Gettysberg Address</p>
        <br />
        <p><a href="brainbashers.com">BrainBashers</a></p>
        <img src="https://media-assets-05.thedrum.com/cache/images/thedrum-prod/s3-news-tmp-90538-cillit_bang_barry_scott--default--1280.jpg" />
        <p>By some guy (some time) [Public domain], via some place</p>
        </body>
        </html>'''

    return [page.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()