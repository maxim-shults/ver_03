# from flask import Flask , render_template_string
# from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
# from os.path import exists

# app = Flask(__name__)
#
# @app.route('/')
# def score_server():
#     try:
#         with open('Scores.txt', 'r') as f:
#             score = f.read() #strip()
#             return f'''
#                 <html>
#                 <head>
#                 <title>Scores Game</title>
#                 </head>
#                 <body>
#                 <h1>The score is <div id="Score">{score}</div></h1>
#                 </body>
#                 </html>
#             '''
#
#     except Exception as e:
#         return f'''
#             <html>
#             <head>
#             <title>Scores Game</title>
#             </head>
#             <body>
#             <h1><div id="score" style="color:red">{e}</div></h1>
#             </body>
#             </html>
#         '''
#
# ############## if __name__ == '__main__':
# app.run()

from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from os.path import exists
import threading
import webbrowser

app = Flask(__name__)

@app.route('/')
def score_server():
    score = False
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        score = file.read()
    if score:
        template = '<html><head><title>Scores Game</title></head><body><h1>Your Score is: <div id="score">{{ SCORE }}</div></h1></body></html>'
        return render_template_string(template, SCORE=score)
    else:
        template = '<html><head><title>Scores Game</title></head><body><h1><div id="score" style="color:red">{{ error }}</div></h1></body></html>'
        return render_template_string(template, error=BAD_RETURN_CODE)

# if __name__ == '__main__':
#     url = 'http://127.0.0.1:5000'
#     threading.Timer(1.25, lambda: webbrowser.open(url)).start()
#app.run()