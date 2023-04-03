from ast import Num
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row = 8, column = 8, color1= 'black', color2 = 'red')


@app.route('/4')
def index1():
    return render_template('index.html', row=4, column=4, color1='green', color2='yellow')

@app.route('/4/<num>')
def index2(num):
    return render_template('index.html', row=(int(num)), column=(int(num)), color1='blue', color2='black')




if __name__=="__main__":
    app.run(debug=True)

