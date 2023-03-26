from pro009 import SingletonObject

obj1 = SingletonObject()
obj1.val = "Obj value 1"
print("print obj1: ",obj1)

print("------------------------")

obj2 = SingletonObject()
obj2.val = "Obj value 2"
print("print obj1: ",obj1)
print("print obj2: ",obj2)