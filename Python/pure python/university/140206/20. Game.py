import random

print("sang ...")
print("gheichi...")
print("kaghaz...")

tedad = int(input("bazi 1player bashad ia 2player ?"))

if tedad == 2:
    while True:
        player1 = input("player1 : lotfan harekat khod ra vared konid : ").lower()
        player2 = input("player2 : lotfan harekat khod ra vared konid : ").lower()


        print(player1)
        print(player2)

        if player1 == player2:
            print("mosavi")
        elif player1 == "sang" and player2 == "kaghaz":
            print("player2 win")
        elif player1 == "sang" and player2 == "gheichi":
            print("player1 win")
        elif player1 == "kaghaz" and player2 == "gheichi":
            print("player2 win")
        elif player1 == "kaghaz" and player2 ==  "sang":
            print("player1 win")
        elif player1 == "gheichi" and player2 == "sang":
            print("player2 win")
        elif player1 == "gheichi" and player2 == "kaghaz":
            print("player1 win")
        elif player1 == "exit" or player2 == "exit":
            print("byby")
            break
        else:
            print("harakatet jaleb nabood !")

elif tedad == 1:
    while True:
        player1 = input("player1 : lotfan harekat khod ra vared konid : ").lower()

        # initialization
        player2 = ""

        adad = random.randint(1, 3)
        print(f"adad is : {adad}")

        if adad == 1:
            player2 = "sang"
        elif adad == 2:
            player2 = "kaghaz"
        elif adad == 3:
            player2 = "gheichi"

        print(f"player1 : {player1}")
        print(f"player2 : {player2}")


        if player1 == player2:
            print("mosavi")
        elif player1 == "sang" and player2 == "kaghaz":
            print("player2 win")
        elif player1 == "sang" and player2 == "gheichi":
            print("player1 win")
        elif player1 == "kaghaz" and player2 == "gheichi":
            print("player2 win")
        elif player1 == "kaghaz" and player2 ==  "sang":
            print("player1 win")
        elif player1 == "gheichi" and player2 == "sang":
            print("player2 win")
        elif player1 == "gheichi" and player2 == "kaghaz":
            print("player1 win")
        elif player1 == "exit" or player2 == "exit":
            print("byby")
            break
        else:
            print("harakatet jaleb nabood !")


else:
    print("sang kaghaz gheich 2 nafarast ostad :|")


# ctrl + shift + d