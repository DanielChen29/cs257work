from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    message = f"Welcome to my webpage. Your lucky number is:" 
    number = random.randint(0, 100)
    return render_template("homepage.html", someText = message, someNum = number)

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 
