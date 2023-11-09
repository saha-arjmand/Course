# print
# use(return)



def square(x):
    print(x ** 2)
    return x ** 2


print(type(square(5)))

# call
# area = 3.14 * square(r)

r = 2
area = 3.14 * square(r)
print(area)