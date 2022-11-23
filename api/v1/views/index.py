from flask import jsonify, make_response, request

from api.v1.views import api_view

from models import storage
from models.artist import Artist
from models.track import Track

from query_functions import recommendation, search


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
def recommend():
    '''
    the api route that deals with the recommnedation of tracks
    based on users input
    '''
    artists = request.values.getlist('artists')
    tracks = request.values.getlist('tracks')
    genres = request.values.getlist('genres')
    limit = request.values.get('limit')

    if not artists:
        artists = None
    if not tracks:
        tracks = None
    if not genres:
        genres = None

    response = recommendation(
        artists=artists, tracks=tracks, genres=genres, limit=limit)

    return make_response(jsonify(response[:-1]), response[-1])


@api_view.route('/search', methods=['POST'], strict_slashes=False)
def search_route():
    '''
    route for search query
    '''
    query = request.values.get('search')
    response = search(query=query)
    return make_response(jsonify(response), 200)
