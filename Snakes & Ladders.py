import random

# Snakes and Ladders setup
sandl = {
    # Snakes
    95: 75, 80: 60, 46: 25, 38: 18, 57: 37,
    # Ladders
    3: 22, 8: 26, 20: 41, 15: 44, 36: 55, 50: 67, 63: 81, 71: 92
}

# Function to handle snakes and ladders
def issafe(sl, newpos):
    if newpos in sl:
        if newpos > sl[newpos]:
            print("Oh no! Bitten by a snake!")
        else:
            print("Great! Climbed a ladder!")
        return sl[newpos]
    else:
        return newpos

# Function to display the board
def printboard(sandl, pos1, pos2):
    snakes = {k: v for k, v in sandl.items() if k > v}
    ladders = {k: v for k, v in sandl.items() if k < v}
    
    for row in range(10, 0, -1):
        for col in range(1, 11):
            num = (row - 1) * 10 + col
            if num == pos1:
                print("[p1]", end=" ")
            elif num == pos2:
                print("[p2]", end=" ")
            elif num in snakes:
                print("[s]", end=" ")
            elif num in ladders:
                print("[l]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

# Initialize player positions
pos1 = 1
pos2 = 1

# Print the initial board
printboard(sandl, pos1, pos2)

# Dice rolling function
def rand():
    return random.randint(1, 6)

# Gameplay loop
curr = 1  # Start with player 1
while pos1 < 100 and pos2 < 100:
    if curr == 1:
        print("Player 1 is at position", pos1)
        input("Press Enter to roll the dice")
        newno = rand()
        print("You rolled a", newno)
        print("__" * 20)
        pos1 += newno
        if pos1 > 100:
            pos1 -= newno  # Stay in place if exceeding 100
        else:
            pos1 = issafe(sandl, pos1)
        printboard(sandl, pos1, pos2)
        print("Player 1's new position is", pos1)
        print("_" * 20)
        curr = 2
    else:
        print("Player 2 is at position", pos2)
        input("Press Enter to roll the dice")
        newno = rand()
        print("You rolled a", newno)
        print("__" * 20)
        pos2 += newno
        if pos2 > 100:
            pos2 -= newno  # Stay in place if exceeding 100
        else:
            pos2 = issafe(sandl, pos2)
        printboard(sandl, pos1, pos2)
        print("Player 2's new position is", pos2)
        print("_" * 20)
        curr = 1

# Declare winner
if pos1 >= 100:
    print("Congratulations! Player 1 wins!")
else:
    print("Congratulations! Player 2 wins!")
