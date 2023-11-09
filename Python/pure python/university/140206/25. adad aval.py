adad = int(input("adad khod ra vared konid : "))

# 23 23 1
# 24 1, 2, 3, 4, 6, 8, 12


parcham = False

if adad > 1:
    for i in range(2, adad):
        if adad % i == 0:
            parcham = True
            break


if parcham == True:
    print(f"adad {adad} aval nist")
else:
    print("adad aval ast")