import spotipy

from spotipy import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException

from sqlalchemy.exc import IntegrityError

from models import storage
from models.artist import Artist
from models.track import Track

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def save_json_to_database(obj):
    '''
    data in obj are being saved to data base from obj
    '''
    track = {}
    artist = {}
    if 'artist_id' in obj:
        artist['id'] = obj.get('artist_id')
        artist['name'] = obj.get('artist_name')
        new_artist = Artist(**artist)
        try:
            storage.new(new_artist)
        except IntegrityError:
            pass

    if 'id' in obj:
        track['id'] = obj.get('id')
        track['title'] = obj.get('title')
        track['preview_url'] = obj.get('preview_url')
        track['image_url'] = obj.get('image_url')
        track['artist_id'] = obj.get('artist_id')
        new_track = Track(**track)
        storage.new(new_track)

    try:
        storage.save()
    except IntegrityError:
        storage.rollback()
        storage.save()


def search(query, type="track", limit=10):
    '''
    search function uses user search query to find songs using spotify search api
    the result is a list of all track details
    '''

    result = sp.search(query, type=type, limit=limit)

    if result and type == "track":
        tracks = get_details_from_json(result)
        save_json_to_database(tracks)
        return tracks

    elif type == "artist":
        result = sp.search(query, type=type, limit=limit)
        result = result.get('artists').get('items')[0]
        artist = {}

        artist['artist_name'] = result.get('name')
        artist['artist_id'] = result.get('id')
        save_json_to_database(artist)

        return artist


def convert_name_to_id(query, type="track"):
    '''
    converts a list of names into their ids
    '''
    result = []
    if not isinstance(query, list):
        s_result = sp.search(query, type=type, limit=1)
        type_ = type + 's'
        s_result = s_result.get(type_).get('items')[0]
        s_result = s_result.get('id')
        result.append(s_result)

    else:
        type_ = type + 's'
        for _ in query:
            s_result = sp.search(_, type=type, limit=1)
            s_result = s_result.get(type_).get('items')[0]
            s_result =  s_result.get('id')
            result.append(s_result)
    
    return result


def get_details_from_json(dct):
    '''
    gather track details from api results
    dct should be a dictionaries response from the api
    '''
    details =[]
    tracks = dct.get('tracks')
    if type(tracks) == dict:
        tracks = tracks.get('items', dct.get('tracks'))

    for track in tracks:
        track_details = {}
        track_details['id'] = track.get('id')
        track_details['title'] = track.get('name')
        track_details['artist_id'] = track.get('artists')[0].get('id')
        track_details['artist_name'] = track.get('artists')[0].get('name')
        track_details['preview_url'] = track.get('preview_url')
        track_details['image_url'] = track.get('album').get(
            'images')[0].get('url')
        details.append(track_details)

    return details


def recommendation(**kwargs):
    '''
    recommendation takes user input and gives back music recommendation
    the argument is a key value argument containing 'artists', 'tracks',
    'genres' and 'limit'
    '''
    tracks = kwargs.get('tracks')
    artists = kwargs.get('artists')
    genres = kwargs.get('genres')
    limit = kwargs.get('limit', 10)

    if tracks:
        tracks = convert_name_to_id(tracks, 'track')
    if artists:
        artists = convert_name_to_id(artists, 'artist')

    try:
        recommendations = sp.recommendations(
            seed_artists=artists, seed_tracks=tracks,
            seed_genres=genres, limit=limit, type='track'
        )
        print(len(recommendations))
    except SpotifyException as e:
        return [{"error": "calling recommendation without artist, genre or track"}, 400]

    recommendations = get_details_from_json(recommendations)
    for _ in recommendations:
        save_json_to_database(_)
    # append the response to be used by the make_response function
    recommendations.append(200)

    return recommendations
