

class Standard:

    def __init__(self, charkh, farmoon, dar):

        self.charkh = charkh
        self.farmoon = farmoon
        self.dar = dar


    def sorat(self):
        print("max speed = 400")




class Peraid(Standard):

    def __init__(self, charkh, farmoon, dar):
        self.charkh = charkh
        self.farmoon = farmoon
        self.dar = dar





a113 = Peraid(4, "bale", "bale")

# a113.sorat()

print(type(a113))