from pydoc import doc
import random

def guess(top_limit):
    random_number = random.randint(1, top_limit)
    user_number = int(input(f"Guess the number between 1 and {top_limit}: "))
    counter=1
    while(random_number!=user_number):
        if(random_number<user_number):
            clue = "lower"
        elif(random_number>user_number):
            clue = "haier"
        user_number= int(input(f"Try a {clue} number: "))
        counter+=1
    print(f"You got the correct number in {counter} tries, it is: {user_number}.")

limit = input("Enter the top limit for the guess the number game: ")
guess(int(limit))
