#!/usr/bin/python3
"""Module that should display input calls"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def app_teardown(exception):
    """Handles teardown"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def list_state():
    """Method that handles listing for state and cities to HTML"""
    state = storage.all('State')
    return render_template('7-states_list.html', state=state)

