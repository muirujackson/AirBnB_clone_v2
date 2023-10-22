#!/usr/bin/python3
"""
a script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
fetching data from the storage engine
"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of State objects from the database."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


# Configure the application to listen on 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
