from tkinter import *
from .widgetBase import *

class TextBoxOBJ(widget):

    def draw(self):
        obj = Entry(self.window)
        obj.pack()
        self.obj = obj
        return obj, self.window
        pass

    
