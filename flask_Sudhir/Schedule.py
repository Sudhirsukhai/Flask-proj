'''
Sudhir Sukhai
03/07/2024
description: A basic flask program
'''
import webbrowser
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template("StudentSchedule.html")
    else:
        GetInfo()
        return render_template("StudentSchedule.html")

def GetInfo():
    global out
    #classes
    CL1 = request.form.get('txtCl1')
    CL2 = request.form.get('txtCl2')
    CL3 = request.form.get('txtCl3')
    CL4 = request.form.get('txtCl4')
    CL5 = request.form.get('txtCl5')
    CL6 = request.form.get('txtCl6')
    CL7 = request.form.get('txtCl7')
    CL8 = request.form.get('txtCl8')
    CL9 = request.form.get('txtCl9')
    #Teachers
    Te1 = request.form.get('txtTe1')
    Te2 = request.form.get('txtTe2')
    Te3 = request.form.get('txtTe3')
    Te4 = request.form.get('txtTe4')
    Te5 = request.form.get('txtTe5')
    Te6 = request.form.get('txtTe6')
    Te7 = request.form.get('txtTe7')
    Te8 = request.form.get('txtTe8')
    Te9 = request.form.get('txtTe9')
    #Room nums
    Rm1 = request.form.get('txtRm1')
    Rm2 = request.form.get('txtRm2')
    Rm3 = request.form.get('txtRm3')
    Rm4 = request.form.get('txtRm4')
    Rm5 = request.form.get('txtRm5')
    Rm6 = request.form.get('txtRm6')
    Rm7 = request.form.get('txtRm7')
    Rm8 = request.form.get('txtRm8')
    Rm9 = request.form.get('txtRm9')

    return render_template{"ScheduleDisp.html",Rm1 = Rm1, }

@app.route("/post")
def post():
    return out

    
if __name__ == "__main__":
    app.run()
