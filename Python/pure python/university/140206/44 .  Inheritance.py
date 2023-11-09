

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print("salam ahvale shoma")



class TenYearOldPerson(Person):

    def __init__(self, name):
        super().__init__(name, 10)


    def greet(self):
        print("chetori :| ")




person_10_sale = TenYearOldPerson("karim")

print(person_10_sale.age)
print(person_10_sale.name)
print(person_10_sale.greet())