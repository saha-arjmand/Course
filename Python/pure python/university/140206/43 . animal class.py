
class Animal:

    def __init__(self, name, age, tedadpa):
        
        self.name = name
        self.age = age
        self.tedadpa = tedadpa


    def speak(self):
        print(f"I am {self.name} and I am {self.age} and I have {self.tedadpa} legs .")



# instance
animal1 = Animal("sag", 3, 4)
animal1.speak()