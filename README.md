*THIS IS CURRENTLY IN BETA*

# web-fw

Hey Guys! Sushant Here,

So Do You Need A *Fast*, *Lightweight* And *Reliable* Web Framework for your Next WebApp?

Here Comes Black Blaze into play

**Black Blaze-WEBfw** is a minimalistic web framework for python.

0. Install Black Blaze-Webfw
   ```
   sushant@H4CK3R:~$ python -m pip install BlackBlazeFw
   ```

1. Import Black Blaze-Webfw:
   ```python
   from BlackBlazeFw import WebApp
   ```

2. Create An App:
   ```python
   app = webApp("__init__", "GUNICORN")
   ```
3. Register URLs:
   ```python
      @app.catchURL('/hello')
      def hello(response):
      ...
   ```

4. Handle Output:
   a. Output HTML:
     ```python
        @app.catchURL('/hello')
        def hello(response):
          response.text = "<b>Hello World</b>"
     ```
     
   b. Set Status Code:
     ```python
        @app.catchURL('/hello')
        def hello(response):
          response.text = "<b>Not Found</b>"
          response.status_code = 404
     ```
     
5. Run The WebApp:
   Create a new file named ```app.py```
   Add The Following Code:
   ```python
   from file import app
   app.run("appname")
   ```
   **Change file To The Name Of The Filename And appname To The Name Of The App(here *app*)**
   Run The File
