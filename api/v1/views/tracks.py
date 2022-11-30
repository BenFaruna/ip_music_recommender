from flask import abort, make_response, jsonify, request
from sqlalchemy.exc import IntegrityError, OperationalError

from api.v1.views import api_view

from models import storage
from models.track import Track


@api_view.route('/tracks', methods=['GET'], strict_slashes=False)
def tracks():
    '''returns the total tracks saved in the database'''
    all_tracks = []
    tracks = storage.all(Track)
    for track in tracks:
        all_tracks.append(tracks[track].to_dict())
    return make_response(jsonify(all_tracks))


@api_view.route('/tracks/<id>', methods=['GET'], strict_slashes=False)
def track(id):
    '''gets the details of a song from the database using song id'''
    track = storage.get(Track, id)
    if track:
        return make_response(jsonify(track.to_dict()))
    else:
        abort(404, description='ID does not exist')


@api_view.route('/get_details/<id>', methods=['GET'], strict_slashes=False)
def get_details(id):
    '''gets the details of a song from the database using song id'''
    track = storage.get(Track, id)
    response = track.to_dict()
    response['artist_name'] = track.artist.name
    if response:
        return make_response(jsonify(response))
    else:
        abort(404, description='ID does not exist')


@api_view.route('/tracks', methods=['POST'], strict_slashes=False)
def track_post():
    '''route for adding track entry into the database'''
    query = request.json

    if not query:
        abort(400, description='Invalid query parameters.')

    if 'title' not in query:
        abort(400, description='title key not present.')

    if 'id' not in query:
        abort(400, description='Id key not present.')

    new_track = Track(**query)
    try:
        storage.new(new_track)
        storage.save()
    except IntegrityError as e:
        return make_response(jsonify({'error': e.args}), 500)
    except OperationalError:
        return make_response({
            "error": "Missing key required keys are\
 id, title, artist_id, image_url"}, 500)
    return make_response(jsonify(new_track.to_dict()))


@api_view.route('/tracks/<id>', methods=['DELETE'], strict_slashes=False)
def tracks_delete(id):
    '''route for deleting track entry from database'''
    query = storage.get(Track, id)
    if query:
        storage.delete(query)
        storage.save()
        return make_response(jsonify({}), 200)
    else:
        return make_response({'error': 'invalid track key'}, 500)
