from tkinter import *
from .widgetBase import *

class ButtonOBJ(widget):

    def setOnClick(self, addr):
        self.attributes["onClick"] = addr

    def draw(self):
    #try:
        
        #print(getattr(self.window, self.attributes["onClick"]))
        obj = Button(self.window, text=self.attributes["text"], command=getattr(self.winOBJ, self.attributes["onClick"]))#getattr(self.callsClass, self.attributes["onClick"]))
        obj.pack()
        self.obj = obj
        return obj, self.window
    #except Exception as e:
        #print(e)
        obj = Button(self.window, text=self.attributes["text"])
        obj.pack()
        self.obj = obj
        return obj, self.window
    #else:
        raise Exception("An Error Occured")

        pass

    
