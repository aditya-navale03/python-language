class Reactangle:
    def __init__(self,length,breath,height):
        self.length = length
        self.breath = breath
        self.height = height
    def area(self):
        print("area=",self.length*self.breath)
        
    def volume(self):
        print("volume:-",self.length*self.breath*self.height)
        
        
r = Reactangle(1,2,3)
r.area()
r.volume()