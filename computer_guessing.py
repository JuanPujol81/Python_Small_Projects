import random

def computer_guess(my_number, low_limit, top_limit):
    counter=1
    computer_number= random.randint(low_limit, top_limit)
    print(f"{computer_number}")
    while(my_number!=computer_number):
        counter+=1
        if(my_number<computer_number):
            top_limit = computer_number-1
        elif(my_number>computer_number):
            low_limit = computer_number+1
        computer_number= random.randint(low_limit, top_limit)
        print(f"{computer_number}")
    print(f"The computer guessed the number in {counter} tries, the number is: {computer_number}")
    
    

my_number = int(input(f"Enter a number to guess by the computer: "))
low_limit = int(input(f"Enter a minimun limit for the range: "))
top_limit = int(input(f"Enter a maximun limit for the range: "))
if(my_number<low_limit)or(my_number>top_limit):
    print("The number must be between the top and min limits.")
else:
    computer_guess(my_number, low_limit, top_limit)