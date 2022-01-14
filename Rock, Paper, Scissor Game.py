import random

def play():

    user = input("r, p or s ?\n")

    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        print("Computer :", computer, "\nIt's a Tie")
    elif is_win(user, computer):
        print("Computer :", computer, "\nYou won!")
    else:
        print("Computer :", computer, "\nYou Lost :(")

def is_win(player, opponent):
    if ( player == 'r' and opponent == 's') or ( player == 's' and opponent == 'p') or ( player == 'p' and opponent == 'r') :
        return True

play()