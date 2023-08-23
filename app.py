## Create a simple flask application
from flask import Flask, render_template

## create the flask app

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello World</h2>"

@app.route('/welcome')
def welcome():
    return "welcome to the Flask tutorials"


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:text>')
def success(text):
    return "the text is "+ str(text)



if __name__=='__main__':
    app.run(debug=True)
