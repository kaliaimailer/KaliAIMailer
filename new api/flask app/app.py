# app.py

from flask import Flask, render_template
from utilities import say_hello

app = Flask(__name__)

@app.route('/')
def home():
    greeting = say_hello("World")  # Using the function from utilities.py
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
