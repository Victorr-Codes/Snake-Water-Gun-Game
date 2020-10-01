# Snake-Water-Gun-Game
This is a famous game called SNAKE WATER GUN. To play this game simply run this python program in your IDLE.








import random
b = 1
ptsc = 0
ptsy = 0
print("\nWELCOME TO SNAKE,WATER,GUN GAME\n")
print("Choice:snake , water , gun")
while(b<11):

    var = input("\nYour choice\n")
    
    lst = ["snake", "water", "gun"]
    
    a = random.choice(lst)
    
    if var=="snake" and a=="water":
        ptsy = ptsy + 1

    elif var=="water" and a=="snake":
        ptsc = ptsc + 1

    elif var=="gun" and a=="water":
        ptsc = ptsc + 1 

    elif var=="snake"  and a=="gun":
        ptsc = ptsc + 1 

    elif var=="water" and a=="gun":
        ptsy = ptsy + 1 

    elif var=="gun" and a=="snake":
        ptsy = ptsy + 1 

    else:
        ptsy = ptsy + 0
        ptsc = ptsc + 0

    b = b + 1

if ptsy>ptsc:
    print("\nYOU WON THE GAME")
    print("Number of times you won:", ptsy)
    print("Number of times computer won:", ptsc)
    print("Number of times drawn", 10-(ptsy+ptsc))
    print("\nTHANKS FOR PLAYING")
    

elif ptsc>ptsy:
    print("COMPUTER WON THE GAME\n")
    print("Number of times you won:", ptsy)
    print("Number of times computer won:", ptsc)
    print("Number of times drawn", 10-(ptsc+ptsy))
    print("\nTHANKS FOR PLAYING")
    print("BETTER LUCK NEXT TIME")

else:
    print("GAME IS DRAWN")
    print("Number of times you won:", ptsy)
    print("Number of times computer won:", ptsc)
    print("Number of times drawn:",10-(ptsc+ptsy))
    print("\nTHANKS FOR PLAYING")
