from BBWebFw import BBlazeWeb
from BBWebFw.FileRenderer import FileRenderer

app =  BBlazeWeb.webApp("__init__", "GUNICORN")

@app.catchURL('/hello') #Goto host/hello
def hello(response):
       response.text = "Hello world!"

@app.catchURL('/err404') #Goto host/err404
def err404(response):
       response.status_code = 404

app.setError(404, FileRenderer.template("error.html", {"error": 404}))