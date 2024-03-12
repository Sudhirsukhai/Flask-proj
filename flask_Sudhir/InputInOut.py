'''
Sudhir Sukhai
03/05/2024
description: A basic flask program
'''

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("form.html")

if __name__ == "__main__":
    app.run()
