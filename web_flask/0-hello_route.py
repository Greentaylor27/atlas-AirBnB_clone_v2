#!/usr/bin/python3
"""Backend api that will hopefully display Hello HBNB"""
from flask import Flask


app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
