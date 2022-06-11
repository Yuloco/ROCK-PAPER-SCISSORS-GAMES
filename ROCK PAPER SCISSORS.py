from ast import And
import random
print("\n Enter: \n R for Rock \n P for Paper \n S for Scissors")
#create a list of play options
t = ["R", "P", "S"]
#set player to False
player = False

while player == False:
#set player to True
    player = input("\n Enter Your Choice: ")
    if player =="R":
        play = "Rock"
    elif player =="P":
        play = "Paper"
    elif player == "S":
        play = "Scissors"
    else:
        player=False
        play = "Invalid Choice"
    print("\n Player: " + play)
    
#assign a random play to the computer   
    computer = random.choice(t)
    if computer =="R":
        comp = "Rock"
    elif computer =="P":
        comp = "Paper"
    elif computer == "S":
        comp = "Scissors"
    if play == "Invalid Choice":
        comp = "CPU can't choose"
    print ("\n CPU: " + comp)
    if player == computer:
        print("\n Tie!")
    elif player == "R":
        if computer == "P":
            print("\n You lose!", comp, "beats", play)
        else:
            print("\n You win!", play, "beats", comp)
    elif player == "P":
        if computer == "S":
            print("\n You lose!", comp, "beats", play)
        else:
            print("\n You win!", play, "beats", comp)
    elif player == "S":
        if computer == "R":
            print("\n You lose...", comp, "beats", play)
        else:
            print("\n You win!", play, "beats", comp)
    else:
        print("\n Invalid Entry. Try Again!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = random.choice(t)