import random
b = 1
ptsc = 0
ptsy = 0
print("\nWELCOME TO SNAKE,WATER,GUN GAME\n")
print("Choice:snake , water , gun")

while(b<6):
    var = input("\nYour choice\n")
    lst = ["snake", "water", "gun"]
    a = random.choice(lst)
        
    if var=="snake" and a=="water":
        print("Computer's Choice:", a)
        print("'You won'")
        ptsy = ptsy + 1

    elif var=="water" and a=="snake":
        print("Computer's Choice:", a)
        print("'Computer won'")
        ptsc = ptsc + 1

    elif var=="gun" and a=="water":
        print("Computer's Choice:", a)
        print("'Computer won'")
        ptsc = ptsc + 1 

    elif var=="snake"  and a=="gun":
        print("Computer's Choice:", a)
        print("'Computer won'")
        ptsc = ptsc + 1 

    elif var=="water" and a=="gun":
        print("Computer's Choice:", a)
        print("'You won'")
        ptsy = ptsy + 1 

    elif var=="gun" and a=="snake":
        print("Computer's Choice:", a)
        print("'You won'")
        ptsy = ptsy + 1 

    else:
        print("Computer's Choice:", a)
        print("'Draw'")
        continue

    b = b + 1


if ptsy>ptsc:
    print("\nYOU WON THE GAME")
    print("Number of times you won:", ptsy)
    print("Number of times computer won:", ptsc)
    print("\nTHANKS FOR PLAYING")
    

elif ptsc>ptsy:
    print("COMPUTER WON THE GAME\n")
    print("Number of times you won:", ptsy)
    print("Number of times computer won:", ptsc)
    print("\nTHANKS FOR PLAYING")
    print("BETTER LUCK NEXT TIME")

else:
    print("\nTHANKS FOR PLAYING")
