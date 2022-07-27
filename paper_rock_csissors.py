import random

def play():
    user=input("Insert 'p' for paper, 'r' for rock, 's' for scissors: ")
    computer=random.choice(['p','r','s'])
    print(f"Computer choice: {computer}")
    if user==computer:
        return "Tie"
    if wins(user, computer):
        return("User wins")
    else:
        return("Computer wins")

def wins(player, opponent):
    if(player=='p' and opponent=='r')or(player=='r' and opponent=='s')or(player=='s' and opponent=='p'):
        return True
    else:
        return False
    


print(play())
