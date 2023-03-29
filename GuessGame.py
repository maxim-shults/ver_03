import random


def generate_number(difficulty):
    return random.randint(1, int(difficulty))

def get_guess_from_user(difficulty):
    difficulty = int(difficulty)
    guess = input(f"Guess a number between 1 and {difficulty} : ")
    # while not guess.isdigit() or int(guess) < 1 or int(guess) > difficulty:
    #     guess = input(f"Invalid input. Please guess a number between 1 and {difficulty}: ")
    return int(guess)

def compare_results(secret_number, guess):
    if guess == secret_number:
        print("Congratulations, you won!")
        return True
    else:
        print(f"Sorry, the number was {secret_number}. You lost.")
        return False

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)



