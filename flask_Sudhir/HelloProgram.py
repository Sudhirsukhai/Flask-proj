'''
Sudhir Sukhai
2/26/2024
description: A basic flask program
'''
from flask import Flask

app = Flask(__name__) #Create an instance of a flask web application

@app.route("/") #Access specific page

def main():
    return"Hello. This is the main program!<h1>Hello</h1>"

if __name__ == "__main__":
    app.run()
