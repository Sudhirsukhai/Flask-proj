'''
Sudhir Sukhai
03/07/2024
description: A basic flask program
'''
import webbrowser
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template("GetandPost.html")
    else:
        post()
        return render_template("GetandPost.html")

@app.route("/post")
def post():
    name = request.form.get('txtname')
    email = request.form.get('txtemail')
    output = "Hello " + name + ". Thank you for your email " + email
    return "This is your info<ol><tr>"+ output +"</tr></ol>"

    
if __name__ == "__main__":
    app.run()
