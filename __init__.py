import os, sys, re
from BBWebFw import backend

class webApp:
    def __init__(self, name, server):
        self.urls = {}
        self.server = server
        self.name = name
        self.error = {"urlcatcherexists" : "ERR:URL_CATCHER_ALREADY_EXISTS"}
        backend.api(name, server)

    def __call__(self, environ, start_response):
        return backend.api.__call__(self, environ, start_response)
    
    def catchURL(self, path):
        return backend.api.catchURL(self, path)


    def run(self, app, debug=False):
        backend.api.run(self, app)

    def handle_request(self, request):
        return backend.api.handle_request(self, request)
    
    def find_handler(self, request):
        return backend.api.find_handler(self, request)

    def err404(self,response):
        return backend.api.err404(self, response)

    def setError(self, code, data):
        return backend.api.setError(self, code, data)






















'''
def run(self, app, debug=False):
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
        if debug: 
            with open(self.fname) as f:
                self.old = f.read()
                while True:
                    print("11")
                    with open(self.fname) as f:
                        if f.read() == self.old:
                            print("12")
                            self.old = f.read()
                            print("changed!!!")

                        time.sleep(5)
        else:
            backend.run()
        
'''