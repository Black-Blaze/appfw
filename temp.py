import os
from xml.etree import ElementTree as XMLParser
from tkinter import *
from .button import *
from .edittext import *


class Page:
    def __init__(self, xmlFile, title="home", size="350x200"):
        #try:
        root = Tk()
        root.title(title)
        root.geometry(size)
        def textview(attributes):
            return TextViewOBJ(attributes, root).draw()
            
        def edittext(attributes):
            return TextBoxOBJ(attributes, root).draw()

        def checkbox(attributes):
            return ButtonOBJ(attributes, root).draw()
        '''    
        def radiobox(attributes):
            return TextViewOBJ(attributes, root).draw()
            
        def layout(attributes):
            return TextBoxOBJ(attributes, root).draw()

        def listview(attributes):
            return ButtonOBJ(attributes, root).draw()

        def spinnerlist(attributes):
            return TextViewOBJ(attributes, root).draw()
            
        def menu(attributes):
            return TextBoxOBJ(attributes, root).draw()

        def menuitem(attributes):
            return ButtonOBJ(attributes, root).draw()'''

        self.XML = XMLParser.fromstring(open(os.path.abspath('app.xml'), "rb").read())
        self.elements = {
            "textview":textview,
            "edittext":edittext,
            "button":button,
        }
            '''"checkbox":checkbox,
            "radiobox":radiobox,
            "layout":layout,
            "listview":listview,
            "spinnerlist":spinnerlist,
            "menu":menu,
            "menuitem":menuitem,'''
        self.objects = {}
        for child in self.XML:
            print(child.tag, child.attrib)
            obj, root = self.elements[child.tag](child.attrib)
            self.objects.update()

        #a.pack()
        print(self.XML)
        self.root = root
        pass
        #except Exception as e:
        #    print(e)

    def display(self):
        self.root.mainloop()
        pass