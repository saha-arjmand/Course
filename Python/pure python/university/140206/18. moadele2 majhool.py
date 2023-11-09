import math


a = float(input("a ra vareed konid : "))
b = float(input("b ra vareed konid : "))
c = float(input("c ra vareed konid : "))


delta = (b ** 2) - (4 * a * c)


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"moadele 2 rishe darad x1 = {round(x1,2)} , x2 = {round(x2,2)}")

elif delta == 0:
    x = -b / (2 * a)
    print(f"rishe mozaf barbar ast ba {x}")
else:
    print("moadele rishe nadarad")