from random import randint
import pandas as pd


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
            print ("\nChoose one of the options!")
            

def practicing():
    words_correct_index = []
    contador = 0    
    data = pd.read_csv("data.csv")
    print("\n" + "\033[1;34m-\033[0m" * 20 +"\033[1;34mS-T-A-R-T-I-N-G\033[0m" + "\033[1;34m-\033[0m" * 20)
    print("\033[1;34mTry to guess the word bellow or write 'q' to Quit:\033[0m\n")
    
    while contador != len(data):

        random_number = randint(0, len(data))        

        if random_number == len(data):
            continue
        if random_number in words_correct_index:
            continue
        
        correct_answer = str(data["traduction"][random_number])
        correct_answer = list(correct_answer.split(";"))

        print("-> Give the traduction of the word or write 'q' to Quit:")
        user_answer = (input(f"           {data["word"][random_number]} -> "))
        
        if user_answer in correct_answer:
                if len(correct_answer) > 1:
                    print(data)
                    print("\033[32m-\033[1m" * 20 + "\033[32mCORRECT!\033[0m" + "\033[32m-\033[0m" * 20 + "\n")    
                    print(f"\033[32m            {correct_answer}\033[0m"+ "\n")    
                else: 
                    print("\033[32m-\033[1m" * 20 + "\033[32mCORRECT!\033[0m" + "\033[32m-\033[0m" * 20 + "\n")    
                words_correct_index.append(int(random_number))
                contador += 1

        elif user_answer == "q":
            print ("\033[32mThanks for use the app! See you soon!\033[0m")
            break
        
        else:
            print("\033[31m-\033[1m" * 20 + "\033[1;31mINCORRECT!\033[1;41" + "\033[31m-\033[0m" * 20)
            print(f"\033[1;33m         Correct Answer -> {correct_answer}\n\033[0m")
    else: print("\033[1;95mYou finished the words! CONGRATULATIONS\033[1;105")

def app():
    response = starting_app()
    if response == "1":
        practicing()

app()