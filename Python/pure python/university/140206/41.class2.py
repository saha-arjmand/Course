
# class
class charzeli:
    
    def __init__(self, tool , arz):
        # properties
        self.tool = tool
        self.arz = arz

    # method
    def masahat(self):
        masahat = self.tool * self.arz
        return masahat
    
    def mohit(self):
        mohit = (self.tool *2) + (self.arz * 2)
        return mohit
    


# instance (object)
moraba = charzeli(5, 5)
print(moraba.masahat())
print(moraba.mohit())


mostatil = charzeli(5, 2)
print(mostatil.masahat())
print(mostatil.tool)
print(mostatil.mohit())


