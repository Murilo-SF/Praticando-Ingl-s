from random import randint
import pandas as pd

data = pd.read_csv("data.csv")

words = {"Apple":"Maçã", "Orange":"Laranja"}
keys = list(words.keys())

def starting_app():
    print("\033[34m-\033[1m" * 20 +"\033[34mP-R-A-C-T-I-C-I-N-G| | | | |E-N-G-L-I-S-H\033[0m" + "\033[34m-\033[0m" * 20)
    print("-> Select one of the options:")
    while True:
        response = input(str(
            '''
            1. Start
            2. Exit
            Response: '''
        ))
        if response == "1": 
            return response
        elif response == "2":
            print ("Thanks for use the app! See you soon!")
            break
        else: 
            print ("\nChose one of the options!")
            

def practicing():
    print("\n" + "-" * 20 +"S-T-A-R-T-I-N-G" + "-" * 20)
    while True:
        random_number = randint(0, (len(words)-1))
        
        print("-> Give the traduction of the word:")
        answer = input(str(f"           {keys[random_number]} -> "))
        
        if answer == words[str(keys[random_number])]:
            print("\033[32m-\033[0m" * 20 + "\033[32mCORRECT ANSWER!\033[0m" + "\033[32m-\033[0m" * 20 + "\n")    
        
        else:
            print("\033[31m-\033[0m" * 20 + "\033[1;31mINCORRECT ANSWER!\033[1;41" + "\033[31m-\033[0m" * 20 + "\n")    

def app():
    response = starting_app()
    if response == "1":
        practicing()

app()