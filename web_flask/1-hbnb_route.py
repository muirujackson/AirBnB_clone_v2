#!/usr/bin/python3
""" create a script that starts a Flask web application """


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
