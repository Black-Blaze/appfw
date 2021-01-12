from tkinter import *
from .widgetBase import *
from .button import *
from .edittext import *
from .textview import *
from .layout import *

class LayoutOBJ(widget):
    def textview(self, attributes, obj):
        return TextViewOBJ(attributes, obj, self.winOBJ)#, self.callsClass)
        
    def edittext(self, attributes, obj):
        return TextBoxOBJ(attributes, obj, self.winOBJ)#, self.callsClass)

    def button(self, attributes, obj):
        return ButtonOBJ(attributes, obj, self.winOBJ)#, self.callsClass)

    def layout(self, attributes, obj):
        return LayoutOBJ(attributes, obj, self.winOBJ)#, self.callsClass)

    def setOnClick(self, addr):
        self.attributes["onClick"] = addr

    '''"checkbox":checkbox,
        "radiobox":radiobox,
        "listview":listview,
        "spinnerlist":spinnerlist,
        "menu":menu,
        "menuitem":menuitem,'''

    def getChildren(self):
        for child in self.object:
            #print(child.tag, child.attrib)
            self.objects[child.attrib["id"]] = self.elements[child.tag](child.attrib, child)
            obj, root = self.objects[child.attrib["id"]].draw()

    def draw(self):
        self.elements = {
            "textview":self.textview,
            "edittext":self.edittext,
            "button":self.button,
            "layout":self.layout,
        }
        self.objects = {}
        #print(self.attributes)
        obj = Frame(self.window, bg=self.attributes["background"], pady=self.attributes["paddingY"], padx=self.attributes["paddingX"])
        obj.pack()
        self.obj = obj
        self.getChildren()
        return obj, self.window