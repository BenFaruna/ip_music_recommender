#!/usr/bin/python3

'''module defining routing and logic of backend'''
from flask import Flask, render_template
# from flask_cors import CORS

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.route("/", strict_slashes=False)
def index():
    '''route to the homepage of the web application'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)