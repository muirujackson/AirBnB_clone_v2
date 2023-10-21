#!/usr/bin/python3
""" create a script that starts a Flask web application """


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ This function return a hello message """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This method diplay 'HBNB' """
    return "HBNB"

@app.route('/c/<text>', strct_slashe=False)
def ctext(text):
    """ this method 'c' followed by value of text """
    return f"C {escape(text)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
