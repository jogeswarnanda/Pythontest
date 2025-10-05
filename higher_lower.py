import random
import re
import gamedata

def generate_random():
    score = 0
    game_shoud_continue = True
    account_b = random.choice(gamedata.data)
    while game_shoud_continue:
        account_a =account_b
        account_b =random.choice(gamedata.data)
        if account_a == account_b:
            account_b = random.choice(gamedata.data)
        print(f"Compare A:", {format_data(account_a)})
        print("VS")
        print(f"Compare B:", {format_data(account_b)})
        a_follower = account_a["Follower"]
        b_follower = account_b["Follower"]
        #print("af", a_follower)
        #print("bf", b_follower)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        print("\n"* 20)
        iscorrect = check_guess(guess,a_follower,b_follower)
        print("Answer", iscorrect)
        if iscorrect:
            score += 1
            print("You'r Right!. Your Score :", score)
        else:
            print("You lost!. Your Final Score :", score)
            game_shoud_continue = False

def check_guess(guess, a_follower, b_follower):
    if a_follower > b_follower :
        return guess == 'a'
    else:
        return guess == 'b'


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

print("Welcome to the Higher Lower Game!")
generate_random()
score = 0
print("You've lost the game! Final score: ",score)

