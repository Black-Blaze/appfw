class widget():
    def __init__(self, attributes, obj, winOBJ):#, callsClass):# text="BUTTON", width=100, height=50, corner_radius=25, border_weight=1):
        self.attributes = attributes
        self.object = obj
        self.winOBJ = winOBJ 
        self.window = winOBJ.root
        #self.callsClass = callsClass
        pass

    def setText(self, text):
        self.obj.configure(text=text)
        pass

    def getText(self, text):
        return self.text
        pass

    def setHeight(self, height):
        self.height = height
        pass

    def getHeight(self, height):
        return self.height
        pass

    def setWidth(self, width):
        self.width = width
        pass

    def getWidth(self, width):
        return self.width
        pass