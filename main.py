from art import logo, vs
from game_data import data
import random
import os
# Display the art
def foramat_data(account):
    '''Takes the account data and print it to printable format '''
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f" {account_name}, a {account_descr} from {account_country} "

def check_answer(guess, a_followers, b_follwers):
    """Take the guess and follower counts and returns if they got it right """
    if a_followers>b_follwers:
        return guess=="a"
    else:
        return guess=="b"

score = 0

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b 
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {foramat_data(account_a)}")
    print(vs)
    print(f"Against B: {foramat_data(account_b)}")

    # Ask user for a guess

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()


    # Check if user is correct

    ## Get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # use if condtion to check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    
    os.system("cls")
    print(logo)
    # Give user feedback on thier gues
    # Score keeping
    if is_correct:
        score+=1
        print(f"You're right!, you are current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, That's wrong! you are final score is {score}")


    # Make the game repeatable

    # make the acount position at B and next account position at A.

    # Clear the Screen b/w the rounds
