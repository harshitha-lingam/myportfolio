
from flask import Flask, request,redirect,url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<center>Welcome to Flaskapp</center>"


@app.route('/greet/<uname>')
def greet(uname):
    return f'<center>Good morning!, {uname}</center>'

@app.route('/user',methods= ['GET' , 'POST'])
def myProfile():
    data=None
    if request.method == 'POST':
        data=request.form
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)