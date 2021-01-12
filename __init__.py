import os
from xml.etree import ElementTree as XMLParser
from tkinter import *
from tkinter.ttk import *
from .button import *
from .edittext import *
from .textview import *
from .layout import *


class Page(object):
    def __init__(self, xmlFile):#, callsClass=None, title="home", size="350x200"):
        #print(Checkbutton().keys())
        #try:
        self.root = Tk()
        #callsClass = callsClass()
        def textview(attributes, obj):
            return TextViewOBJ(attributes, obj, self)#, callsClass)
            
        def edittext(attributes, obj):
            return TextBoxOBJ(attributes, obj, self)#, callsClass)

        def button(attributes, obj):
            return ButtonOBJ(attributes, obj, self)#, callsClass)
            
        def checkbox(attributes, obj):
            return TextViewOBJ(attributes, obj, self)#, callsClass)
            
        def radiobox(attributes, obj):
            return TextViewOBJ(attributes, obj, self)#, callsClass)
            
        def layout(attributes, obj):
            return LayoutOBJ(attributes, obj, self)# ,callsClass)    getattr(self.callsClass, self.attributes["onClick"])

        def listview(attributes, obj):
            return ButtonOBJ(attributes, obj, self)#, callsClass)

        def spinnerlist(attributes, obj):
            return TextViewOBJ(attributes, obj, self)#, callsClass)
            
        def menu(attributes, obj):
            return TextBoxOBJ(attributes, obj, self)#, callsClass)

        def menuitem(attributes, obj):
            return ButtonOBJ(attributes, obj, self)#, callsClass)

        self.XML = XMLParser.fromstring(open(os.path.abspath(xmlFile), "rb").read())
        self.SheetElm = self.XML.attrib
        self.elements = {
            "textview":textview,
            "edittext":edittext,
            "button":button,
            "checkbox":checkbox,
            "radiobox":radiobox,
            "layout":layout,
            "listview":listview,
            "spinnerlist":spinnerlist,
            "menu":menu,
            "menuitem":menuitem,
        }
        self.objects = {}
        #print(self.XML)
        #print(callsClass)
        for child in self.XML:
            #print(child.tag, child.attrib)
            self.objects[child.attrib["id"]] = self.elements[child.tag](child.attrib, child)
            obj, root = self.objects[child.attrib["id"]].draw()

        #print(self.XML.keys())#self.WindowStruct = 

        #a.pack()
        self.root = root
        pass
        #except Exception as e:
        #    print(e)

    def display(self):
        self.root.title(self.SheetElm["title"])
        self.root.geometry(self.SheetElm["size"])
        self.root.mainloop()
        pass