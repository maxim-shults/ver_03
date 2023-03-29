# import os
# from Utils import *
#
# def clean_score_file():
#     if os.path.exists("Scores.txt"):
#         os.remove("Scores.txt")
#
# def add_score(difficulty):
#     new_score = int(difficulty) * 3 + 5
#     try:
#         with open("Scores.txt", "r") as file:
#             current_score = int(file.read())
#     except FileNotFoundError:
#         current_score = 0
#
#     total_score = current_score + new_score
#     with open("Scores.txt", "w") as file:
#         file.write(str(total_score))
#import os
from os.path import exists
from Utils import *
def add_score(difficulty):
    #אם לא ניצח אין קובץ
    POINTS_OF_WINNING = int(difficulty) * 3 + 5
    contents = None
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        contents = file.read()
        file.close()
    if contents:
        current_score = int(contents) + POINTS_OF_WINNING
    else:
        current_score = POINTS_OF_WINNING
    file = open(SCORES_FILE_NAME, 'w')
    file.write(str(current_score))
    file.close()
    return current_score