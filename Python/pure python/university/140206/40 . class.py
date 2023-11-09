# blueprint class

# ADAM
class Person:

    # constructor -> متد سازنده کلاس
    def __init__(self, name, age):

        # properties
        self.name = name
        self.age = age

    # method
    def salamkardan(self):
        print("man salam mikonam be shoma ! ")


    # method
    def jighzadan(self):
        print("aaaaaaaaaaaaaaaaaaaaaaaaa")


###################################################

# github -> site 
# instance (نمونه) (شی)

# person1 = Person("ali", 20)
# person1.jighzadan()

# print(person1.name)
# print(person1.age)

# hava = "barani"

# if hava == "barani":
#     person1.jighzadan()
# else:
#     person1.salamkardan()


# person2 = Person("amir", 21)
# person2.salamkardan()
# print(person2.name)
# print(person2.age)


person2 = Person("amir", 30)

# x = 12

print(type(person2))