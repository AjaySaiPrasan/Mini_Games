import random

sandl={95:75,80:60,46:25,38:18,57:37,65:45,70:50,62:42,73:53}

def issafe(sl,newpos):
    if newpos in sl:
        p=sl[newpos]
        print("you have been bitten by a snake")
        return p
    else:
        return newpos

def printboard(sandl,pos,pos2):
    l=list(sandl.keys())  # Changed from values() to keys()
    for row in range(10,0,-1):
        for col in range(1,11):
            num=(row-1)*10+col
            if num==pos:
                print("[p]",end=" ")
            elif num==pos2:
                print("[p2]",end=" ")
            elif num in sandl:
                print("[s]",end=" ")
            elif num in l:
                print("[l]",end=" ")
            else:
                print("[ ]",end=" ")
        print()

pos=1
pos2=1
printboard(sandl,pos,pos2)

def rand():
    return random.randint(1,6)

curr=1  # Start with player 1
while pos < 100 and pos2 < 100:
    if curr == 1:
        print("your player1 is in",pos)
        input("press Enter to play")
        newno=rand()
        print("your lucky no is",newno)
        print("__"*20)
        pos=pos+newno
        if pos > 100:
            pos -= newno  # Stay in place if exceeding 100
        else:
            pos=issafe(sandl,pos)
        printboard(sandl,pos,pos2)
        print("your new position is ",pos)
        print("_"*20)
        print("_"*20)
        curr=2
    else:
        print("your player 2 is in",pos2)
        input("press Enter to play")
        newno=rand()
        print("your lucky no is",newno)
        print("__"*20)
        pos2=pos2+newno  # Fixed: was using pos instead of pos2
        if pos2 > 100:
            pos2 -= newno  # Stay in place if exceeding 100
        else:
            pos2=issafe(sandl,pos2)
        printboard(sandl,pos,pos2)
        print("your new position is ",pos2)
        print("_"*20)
        print("_"*20)
        curr=1

if pos >= 100:
    print("congrats player 1 won the game")
else:
    print("congrats player 2 won the game")