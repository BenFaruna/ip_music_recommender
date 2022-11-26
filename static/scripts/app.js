const genres_list = [
    'acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass',
    'blues', 'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical',
    'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'disney',
    'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage',
    'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle',
    'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian', 'indie', 'indie-pop', 'industrial',
    'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino', 'malay', 'mandopop',
    'metal', 'metal-misc', 'metalcore', 'minimal-techno', 'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode',
    'party', 'philippines-opm', 'piano', 'pop', 'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock',
    'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly',
    'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter',
    'soul', 'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop',
    'turkish', 'work-out', 'world-music']

function choose(choices=genres_list) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
  }

$(document).ready(() => {
    let genreList = "";
    for (let i=0; i < 5; i++) {
        // genreList.push(choose());
        genreList = genreList + "genres=" + choose() + "&";
    }

    url = "http://localhost:5001/api/v1/recommend?" + genreList + "limit=7"

    // $.post(
    //     url,
    //     {},
    //     function (data) {
    //         let songs = '';
    //         $.each(data, function (index, value) {
    //             songs = songs + '<li class="songItem">' +
    //             '<span>' + (index + 1) +
    //             '</span>' +
    //             `<img src="${value.image_url}" alt="${value.title}">` +
    //             '<h5>' + value.title +
    //             '<div class="subtitle">' + value.artist_name +
    //             '</div>' +
    //             `<i class="bi playListPlay bi-play-circle-fill" data-id="${value.id}">` +
    //             '</i>' +
    //             '</h5>' +
    //             '</li>'
    //         });

    //         $('.songList').html(songs);
    //     });
})

$('.search input').keypress(function (event) {
    let keycode = event.which;
	if(keycode == 13){
        let s_query = $('.search-input').val()
        $('.search-input').val(""); // empties the search bar for new searches

        let url = 'http://localhost:5001/api/v1/search?' + 'search=' + s_query
        console.log(s_query);

		$.ajax({
            url: url,
            type: 'POST',
            crossOriginIsolated: false,
            contentType: "application/json",
            data: JSON.stringify({search: s_query}),
            dataType: "json",
            success: function (response) {
                let songs = "";
                $.each(response, function (index, value) { 
                    songs = songs +
                    '<div class="song">' +
                        '<div class="song-image">' +
                            `<img src=${value.image_url} alt=${value.title}>` +
                        '</div>' +
                        '<div class="song-details">' +
                            `<a href=${value.preview_url} target="_blank">` +
                            '<h3 class="song-name">' +
                            value.title +
                            '</h3>' +
                            '<h4 class="artist-name">' +
                            value.artist_name +
                            '</h4>' +
                            '</a>' +
                        '</div>' +
                    '</div>'
                });
                $('.search-result').html(songs);
            },
            error: function () {
                alert("Enter a search query and try again");
            }
        })

	}

})

