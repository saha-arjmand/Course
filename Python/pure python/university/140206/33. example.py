import random


listNumber = []


n = 0

while n < 100:
    x = random.randint(1,1000)
    listNumber.append(x)

    n += 1


print(min(listNumber))
print(max(listNumber))