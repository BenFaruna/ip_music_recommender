import main

from flask import jsonify, make_response, request
from flask_cors import CORS, cross_origin

from api.v1.views import api_view

from models import storage
from models.artist import Artist
from models.track import Track

from query_functions import recommendation, search

# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@api_view.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@api_view.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Artist, Track]
    names = ['artists', 'tracks']

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)


@api_view.route('/recommend', methods=['POST'], strict_slashes=False)
@cross_origin(send_wildcard=True)
def recommend():
    '''
    the api route that deals with the recommnedation of tracks
    based on users input
    '''
    artists = request.values.getlist('artists')
    tracks = request.values.getlist('tracks')
    genres = request.values.getlist('genres')
    limit = request.values.get('limit')
    convert = request.values.get('convert')

    if not artists:
        artists = None
    if not tracks:
        tracks = None
    if not genres:
        genres = None

    response = recommendation(
        artists=artists, tracks=tracks, genres=genres,
        limit=limit, convert=convert
        )

    return make_response(jsonify(response[:-1]), response[-1])


@api_view.route('/search', methods=['POST'], strict_slashes=False)
@cross_origin(send_wildcard=True)
def search_route():
    '''
    route for search query
    '''
    query_s = request.values.get('search')
    limit = request.values.get('limit')
    response = search(query=query_s, limit=limit)
    return make_response(jsonify(response), 200)
