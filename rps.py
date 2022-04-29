import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n") # asks for user input
    computer = random.choice(["r","p","s"]) # makes computers choice

    if user == computer: # Check for tie
        print("It's a tie!")
        fl = full(computer)
        print("The computer used",fl)
        return 'Play again soon!'
    
    if is_win(user,computer): # Check for win
        print("You won!")
        fl = full(computer)
        print("The computer used",fl)
        return 'Play again soon!'             

    else:                   # Check for loss
        print("You lost!")
        fl = full(computer)
        print("The computer used",fl)
        return 'Play again soon!'    

def full(ins): # Change single character to full name choice
    if (ins == 'r'):
        return 'rock'
    if (ins == 'p'):
        return 'paper'
    if (ins == 's'):
        return 'scisscors'

def is_win(player,opponent): # Compare and check for win
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())