import random
toss=random.randint(1,2)
t1=int(input("TOSS TIME\nEnter:\n1 for Heads\n2 for Tails\n"))
choice=0
        
def Youbat():
    print("You are batting")
    s1=0
    for i in range(6):
        x1=random.randint(1,6)
        You=int(input("Enter a number btw 1 to 6:"))
        print("Computer's number:",x1)
        if You>6:
            print("Invalid number")
        elif(x1!=You):
            s1=s1+You
        else:
            print("OUT!!!")
            break
    print("You Score:",s1)
    print()
    print("You are bowling")
    s2=0
    for i in range(6):
        x2=random.randint(1,6)
        Computer=int(input("Enter a number btw 1 to 6:"))
        print("Computer's number:",x2)
        if Computer>6:
            print("Invalid number")
        elif(x2!=Computer): 
            s2=s2+x2
            if(s2>s1):
                print("Computer Score:",s2)
                print()
                print("Computer Won!!!")
                break
        else:
            print("OUT!!!")
            print("Computer Score:",s2)
            break
    if(s1>s2):
        print("You Won!!!")
    if(s1==s2):
        print("TIE!!!")

def Youbowl():
    print("You are bowling")
    s2=0
    for i in range(6):
        Computer=random.randint(1,6)
        x2=int(input("Enter a number btw 1 to 6:"))
        print("Computer number:",Computer)
        if x2>6:
            print("Invalid number")
        elif(x2!=Computer):
            s2=s2+Computer
        else:
            print("OUT!!!")
            break
    print("Computer Score:",s2)
    print()
    print("You are batting")
    s1=0
    for i in range(6):
        x1=random.randint(1,6)
        You=int(input("Enter a number btw 1 to 6:"))
        print("Computer's number:",x1)
        if You>6:
            print("Invalid number")
        elif(x1!=You):
            s1=s1+You
            if(s1>s2):
                print("You Score:",s1)
                print()
                print("You Won!!!")
                break
        else:
            print("OUT!!!")
            print("You Score:",s1)
            break
    if(s2>s1):
        print("Computer Won!!!")
    if(s1==s2):
        print("TIE!!!")

def Computerbat():
    print("You are bowling")
    s2=0
    for i in range(6):
        Computer=random.randint(1,6)
        x2=int(input("Enter a number btw 1 to 6:"))
        print("Computer's number:",Computer)
        if x2>6:
            print("Invalid number")
        elif(x2!=Computer):
            s2=s2+Computer
        else:
            print("OUT!!!")
            break
    print("Computer Score:",s2)
    print()
    print("You are batting")
    s1=0
    for i in range(6):
        x1=random.randint(1,6)
        You=int(input("Enter a number btw 1 to 6:"))
        print("Computer's number:",x1)
        if You>6:
            print("Invalid number")
        elif(x1!=You):
            s1=s1+You
            if(s1>s2):
                print("You Score:",s1)
                print()
                print("You Won!!!")
                break
        else:
            print("OUT!!!")
            print("You Score:",s1)
            break
    if(s2>s1):
        print("Computer Won!!!")
    if(s1==s2):
        print("TIE!!!")

def Computerbowl():
    print("You are batting")
    s1=0
    for i in range(6):
        x1=random.randint(1,6)
        You=int(input("Enter a number btw 1 to 6:"))
        print("Computer's number:",x1)
        if You>6:
            print("Invalid number")
        elif(x1!=You):
            s1=s1+You
        else:
            print("OUT!!!")
            break
    print("You Score:",s1)
    print()
    print("You are bowling")
    s2=0
    for i in range(6):
        Computer=random.randint(1,6)
        x2=int(input("Enter a number btw 1 to 6:"))
        print("Computer number:",Computer)
        if x2>6:
            print("Invalid number")
        elif(x2!=Computer):
            s2=s2+Computer
            if(s2>s1):
                print("Computer Score:",s2)
                print()
                print("Computer Won!!!")
                break
        else:
            print("OUT!!!")
            print("Computer Score:",s2)
            break
    if(s1>s2):
        print("You Won!!!")
    if(s1==s2):
        print("TIE!!!")

if(t1==toss):
    print("You won toss!!\n")
    choice=int(input("Choose 1 for batting.\nChoose 2 for bowling.\n"))
    if choice==1:
        Youbat()
    else:
        Youbowl()
else:
     print("Computer won toss!!\n")
     choice=random.randint(1,2)
     if choice==1:
        print("Computer choosed to bat first") 
        Computerbat()
     else:
        print("Computer choosed to bowl first")
        Computerbowl()
