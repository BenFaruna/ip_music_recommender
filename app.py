#!/usr/bin/python3

'''module defining routing and logic of backend'''
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    '''route to the homepage of the web application'''
    return 'Welcome to IP Music converter'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)