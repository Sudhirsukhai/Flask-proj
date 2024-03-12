'''
Sudhir Sukhai
2/27/2024
description: A basic flask program
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")

def main():
    return"Hello. This is the main program!<h1>Hello</h1><h2>Newline</h2>This is also a new line<br>this is another way<p>This is a paragraph</p>";

if __name__ == "__main__":
    app.run()
