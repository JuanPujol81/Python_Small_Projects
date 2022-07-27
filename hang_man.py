import json
import random

with open("english_dictionary.json","r") as file:
    my_dictionary = list(json.load(file).keys())
user_word = []
joined_letters =""
match_word = random.choice(my_dictionary)
match_list_word = list(match_word)
for letter in match_list_word:
    joined_letters+="_"
    user_word.append("_")
print(f"Match word: \n{joined_letters}")

while(user_word!=match_list_word):
    joined_letters=""
    user_letter=input(f"Guess a letter: ")
    x=0
    for letter in match_list_word:
        if(user_letter==letter and letter in user_word):
            print("You already try that letter. ")
        elif(user_letter==letter):
            user_word[x]=letter
        x+=1
            
    for letter in user_word:
        joined_letters+=letter
    print(joined_letters)
    
print(f"You guessed the word, it is: {joined_letters}")