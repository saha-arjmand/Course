import math

while True:
    num1 = float(input("lotfan adad aval ra vared konid : "))
    num2 = float(input("lotfan adad dovom ra vared konid : "))

    operation = input("lotfan amalgar khod ra vared konid : ")


    if operation == "+":
        natije = num1 + num1
        print(natije)
    elif operation == "-":
        natije = num1 - num2
        print(natije)
    elif operation == "*":
        natije = num1 * num2
        print(natije)
    elif operation == "/":
        natije = num1 / num2
        print(natije)
    elif operation == 'tan':
        print(f"tan {num1} : {math.tan(num1)}")
        print(f"tan {num2} : {math.tan(num2)}")
    else:
        print("meghdar dorost be man bede !")

