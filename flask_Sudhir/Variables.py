'''
Sudhir Sukhai
2/29/2024
description: A basic flask program
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")

def main():
    P1="Welcome to Python Programming Using Flask<br>"
    P2="I am an advanced programmer in developing web sites<br>"
    P3="Make sure to stay tuned for some more fun using Flask"
    return(P1+P2+P3)

if __name__ == "__main__":
    app.run()
