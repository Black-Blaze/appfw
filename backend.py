from webob import Request, Response
from BBWebFw.FileRenderer import FileRenderer
import os, sys, re, datetime
from gunicorn.app.wsgiapp import run as boot

renderfile = FileRenderer()

class api:
    """
    docstring
    """

    def __init__(self, name, server):
        self.urls = {}
        self.server = server
        self.name = name
        self.out404 = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Document</title>\n</head>\n<body>\n    Hello\n</body>\n</html>'
        self.error = {"urlcatcherexists" : "ERR:URL_CATCHER_ALREADY_EXISTS"}
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        #user_agent = request.environ.get('HTTP_USER_AGENT')
        response = Response()
        response.status_code = 200
        response.text = "Blank"
        with open("access-log.txt", "wb") as f:
            f.write(('127.0.0.1 - - ['+(datetime.date.today().__str__())+' '+(datetime.datetime.now().strftime("%H:%M:%S"))+ '] GET / HTTP/1.1" 200').encode())
        
        handler = self.find_handler(request)

        if handler is not None:
            handler(response)
        else:
            self.err404(response)

        return response

    def catchURL(self, path):
        def wrapper(handler):
            if(not(self.urls.__contains__(path))):
                self.urls[path] = handler
                print(self.urls[path])
                return handler
            else:
                print("hi")
                raise AssertionError(self.error["urlcatcherexists"])
                return self.error["urlcatcherexists"]

        return wrapper

    def find_handler(self, request):
        for path, handler in self.urls.items():
            if path == request.path:
                return handler

    def err404(self,response):
        response.status_code = 404
        response.text = self.out404

    def setError(self, code, data):
        if code == 404:
            self.out404 = data
        else:
            raise Exception("Invalid Error Code")

    def run(self, app):
        print("run")
        host = "127.0.0.1"
        port = 6000

        if (self.name).endswith(".py"):
            self.fname = self.name
            self.name = (self.name).replace(".py", "")
        else:
            self.fname = self.name + ".py"
        
        sys.argv = [re.sub(r'(-script\.pyw|\.exe)?$', '', "env/bin/gunicorn"),self.name+':'+ app]
        print(sys.argv)
        sys.exit(boot())