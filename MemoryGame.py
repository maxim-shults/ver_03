import random
import time
import os


def generate_sequence(difficulty):
    seq = [random.randint(1, 101) for i in range(int(difficulty))]
    return seq

def get_list_from_user(difficulty):
    user_seq = []
    for i in range(int(difficulty)):
        num = int(input(f"Enter number {i + 1}: "))
        user_seq.append(num)
    return user_seq

def is_list_equal(seq1, seq2):
    return seq1 == seq2

def play(difficulty):
    seq = generate_sequence(difficulty)
    print("Memorize the sequence:")
    print(seq)
    time.sleep(0.7)
    print("Now, enter the sequence:")
    user_seq = get_list_from_user(difficulty)
    if is_list_equal(seq, user_seq):
        print("Congratulations! You won!")
        return True
    else:
        print("Sorry, you lost.")
        return False


