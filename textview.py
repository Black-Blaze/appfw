from tkinter import *
from .widgetBase import *

class TextViewOBJ(widget):

    def setOnClick(self, addr):
        self.attributes.attrib["onClick"] = addr

    def draw(self):
        obj = Label(self.window, text=self.attributes["text"])
        obj.pack()
        self.obj = obj
        return obj, self.window