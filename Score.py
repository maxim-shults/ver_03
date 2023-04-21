
from os.path import exists
from Utils import *
def add_score(difficulty):
    
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
