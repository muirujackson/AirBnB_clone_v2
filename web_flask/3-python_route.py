#!/usr/bin/python3
""" create a script that starts a Flask web application """


from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ This function return a hello message """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This method diplay 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Replace underscores with spaces in the 'text' variable """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def d_python(text="is cool"):
    """
    This diplate python plus value of text
    underscore in text are replace with space
    """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
