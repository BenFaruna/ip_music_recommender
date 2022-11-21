import spotipy

from spotipy import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def search(query, type="track", limit=10):
    '''
    search function uses user search query to find songs using spotify search api
    the result is a list of all track details
    '''

    result = sp.search(query, type=type, limit=limit)

    if result and type == "track":
        result = result.get("tracks", {}).get("items", [])
        tracks = []
        for track in result:
            track_details = {}
            track_details['id'] = track.get('id')
            track_details['title'] = track.get('name', 'NO TITLE')
            track_details['preview_url'] = track.get('preview_url')
            track_details['artist_id'] = track.get('artists')[0].get('id')
            track_details['artist_name'] = track.get('artists')[0].get('name')

            try:
                track_details['images_url'] = track.get('album').get('images')[0].get('url')
            except IndexError:
                track_details['images_url'] = None
        
            tracks.append(track_details)

        return tracks

    elif type == "artist":
        result = sp.search(query, type=type, limit=limit)
        result = result.get('artists').get('items')[0]
        artist = {}

        artist['name'] = result.get('name')
        artist['id'] = result.get('id')

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
    for track in tracks:
        track_details = {}
        track_details['id'] = track.get('id')
        track_details['title'] = track.get('name')
        track_details['artist_id'] = track.get('artists')[0].get('id')
        track_details['artist_name'] = track.get('artists')[0].get('name')
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

    recommendations = sp.recommendations(seed_artists=artists, seed_tracks=tracks, seed_genres=genres, limit=limit, type='track')
    recommendations = get_details_from_json(recommendations)
    return recommendations


# print(search('BXNX', 'artist', 1))
# print(sp.search("Buju", type='artist', limit=2))

# with open("artist.json", "w") as f:
    # json.dump(sp.search("BNXN", type='artist', limit=2), f, indent=2)

# print(convert_name_to_id(["Kiss me thru the phone", "Barawo", "Loyal"], 'track'))
# print(convert_name_to_id("Chris Brown", 'artist'))
# with open ("recommendation.json", 'w') as f:
#     json.dump(recommendation(artists=["Chris Brown"], genres=["hip hop", "rnb"]), f)
# print(recommendation(genres=["r-n-b", "cantopop"]))
# print(len(sp.recommendation_genre_seeds().get('genres')))