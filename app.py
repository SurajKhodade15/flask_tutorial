## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/adminReroute')
def adminReroute():
    return "<h2>Hello, World! from adminReroute</h2>"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Welcome to the Flask Tutorials, {name}!</h1>"

@app.route('/admin')
def admin():
    return redirect(url_for("adminReroute"))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)


## Assignemnt Try for loop



if __name__=='__main__':
    app.run(debug=True)


