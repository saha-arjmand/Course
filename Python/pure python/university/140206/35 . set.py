# set -> majmooe riazi
# syntax 
# dictionary = {"name":"ali", "family":"hosseinkhani"}
# set = {1,2,3,4,5,6,7,8,8}
# majmoohe ha nazm daran : {1,2,3,4} -> {2,3,4,1}  True
# agar man adad tekrari be in majmooe azafe konam ezafe mishavad ia kheir : {1,1,2,3,4} True


listNumber = {1,2,3,4,5,6,6,6,6,6,6,6,6,6,6,6,1,4,6,8,10, "one"}
listNumber2 = {10, 8, 6, 5, 4, 3, 2, 1}

print(type(listNumber))
print(listNumber)
print(listNumber2)

# for anyItem in listNumber:
#     print(anyItem)

listNumber.add(15)
print(listNumber)

listNumber.clear()
print(listNumber)