
# 10
# 1,2,3,4,5,6,7,8,9
# 3, 5, 6, 9
# 3 + 5 + 6 + 9 = 23


# 1000
# 3 / 5
# sum ?


number = int(input("lotfan iek adad vared konid : "))
rangeadad = range(1, number)


jam = 0

# pep8 _ cleancode
for anyNumber in rangeadad:
    if anyNumber % 3 == 0 or anyNumber % 5 == 0:
        jam = jam + anyNumber


print(jam) 
