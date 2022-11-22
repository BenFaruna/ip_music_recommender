from flask import Blueprint

api_view = Blueprint('api_view', __name__, url_prefix='/api/v1')

from api.v1.views.tracks import *
from api.v1.views.artist import *