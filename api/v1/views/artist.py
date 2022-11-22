from flask import abort, make_response, jsonify, request
from sqlalchemy.exc import IntegrityError

from api.v1.views import api_view
from models.artist import Artist
from models import storage


@api_view.route('/artists', methods=['GET'], strict_slashes=False)
def artists():
    '''returns the total artist saved in the database'''
    all_artists = []
    artists = storage.all(Artist)
    for artist in artists:
        all_artists.append(artists[artist].to_dict())
    return make_response(jsonify(all_artists))


@api_view.route('/artists/<id>', methods=['GET'], strict_slashes=False)
def artist(id):
    '''returns the details of an artist from the database using artist id'''
    artist = storage.get(Artist, id)
    if artist:
        return make_response(jsonify(artist.to_dict()))
    else:
        abort(404, description='ID does not exist')


@api_view.route('/artists', methods=['POST'], strict_slashes=False)
def artist_post():
    '''route for adding artist entry into the database'''
    query = request.json

    if not query:
        abort(400, description='Invalid query parameters.')

    if 'name' not in query:
        abort(400, description='Name key not present.')

    if 'id' not in query:
        abort(400, description='Id key not present.')

    new_artist = Artist(**query)
    try:
        storage.new(new_artist)
        storage.save()
    except IntegrityError as e:
        return make_response(jsonify({'error': 'duplicate key entry'}), 500)
    return make_response(jsonify(new_artist.to_dict()))


@api_view.route('/artists/<id>', methods=['DELETE'], strict_slashes=False)
def artist_delete(id):
    '''route for deleting artist entry from database'''
    query = storage.get(Artist, id)
    if query:
        storage.delete(query)
        storage.save()
        return make_response(query.to_dict(), 200)
    else:
        return make_response({'error': 'invalid artist key'}, 500)