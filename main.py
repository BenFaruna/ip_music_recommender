#!/usr/bin/python3

'''module defining routing and logic of backend'''
from flask import Flask, render_template
from api.v1.views import api_view
from flask_cors import CORS

from models import storage

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(api_view)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.route("/", strict_slashes=False)
def index():
    '''route to the homepage of the web application'''
    return render_template('landing.html')

@app.route("/home", strict_slashes=False)
def home():
    '''route to the homepage of the web application'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)