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

function changePlayerSong(song, start=false) {
    // make changes to the current player song 
    // based on song json passed as argument
    const audio_s = document.querySelector('audio');
    const audio = $('audio');
    audio.attr('src', song.preview_url);
    $('.master_play > img').attr({'src': song.image_url, 'alt': song.artist_name});
    const title = `${song.title}<br>`+`<div class="subtitle">${song.artist_name}</div>`;
    $('.master_play > h5').html(title);
    if (start) {
        toogleAudio();
    }
}

$(document).ready(() => {
    let genreList = "";
    for (let i=0; i < 2; i++) {
        // genreList.push(choose());
        genreList = genreList + "genres=" + choose() + "&";
    }

    url = "https://ip-music-recommender.onrender.com/api/v1/recommend?" + genreList + "limit=7&convert=true"

    $.post(
        url,
        {},
        function (song) {
            let songs = '';
            $.each(song, function (index, value) {
                songs = songs + 
                `<li class="songItem" data-preview-url="${value.preview_url}">` +
                    '<span>' + (index + 1).toString().padStart(2, '0') +
                    '</span>' +
                    `<img src="${value.image_url}" alt="${value.title}">` +
                    '<h5>' + value.title +
                        '<div class="subtitle">' + value.artist_name +
                        '</div>' +
                    `<i class="bi playListPlay bi-play-circle-fill" data-id="${value.id}">` +
                    '</i>' +
                    '</h5>' +
                    '</li>'
                });
                
                $('ul.songList').html(songs);
                changePlayerSong(song[0], false);
            });
        $(window).bind('click', function (e) {
            songEvent();
            $(window).unbind();
        });
        // songEvent();
})

$('.search input').keypress(function (event) {
    let keycode = event.which;
	if(keycode == 13){
        let s_query = $('.search-input').val()
        $('.search-input').val(""); // empties the search bar for new searches

        let url = 'https://ip-music-recommender.onrender.com/api/v1/search?limit=15&' + 'search=' + s_query

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
                    '<li class="song-item">' +
                        `<div class="img_play" data-id="${value.id}">` +
                            `<img src=${value.image_url} alt=${value.title}>` +
                            `<i class="bi playListPlay bi-play-circle-fill" data-id="${value.id}"></i>` +
                        '</div>' +
                        `<div class="song-details" data-id="${value.id}">` +
                            '<h5 class="song-name">' +
                                value.title + '<br>' +
                                '<div class="subtitle">' +
                                value.artist_name +
                                '</div>' +
                            '</h5>' +
                        '</div>' +
                    '</li>'
                });
                $('ul.menu_song').html(songs);
                $.when(songEvent()).done(searchEvent);
            },
            error: function () {
                alert("Enter a search query and try again");
            }
        })
	}

})

function songEvent () {
    let song_list = document.querySelectorAll('.playListPlay');
    song_list.forEach(element => {
        // console.log(element.getAttribute('data-id'));
        element.addEventListener('click', () => {
            $.ajax({
                type: "GET",
                url: "https://ip-music-recommender.onrender.com/api/v1/get_details/" + element.getAttribute('data-id'),
                success: function (response) {
                    changePlayerSong(response, true);
                }
            });
        });
    });
}

function searchEvent () {
    let search_list = document.querySelectorAll('.song-details');
    search_list.forEach(element => {
        element.addEventListener('click', () => {
            // console.log(element);
            let element_id = element.getAttribute('data-id');
            $.ajax({
                type: "POST",
                url: "https://ip-music-recommender.onrender.com/api/v1/recommend?tracks=" + element_id + "&limit=7&convert=false",
                dataType: "json",
                success: function (song) {
                    let songs = '';
                    $.each(song, function (index, value) {
                    songs = songs + 
                    `<li class="songItem" data-preview-url="${value.preview_url}">` +
                        '<span>' + (index + 1).toString().padStart(2, '0') +
                        '</span>' +
                        `<img src="${value.image_url}" alt="${value.title}">` +
                        '<h5>' + value.title +
                            '<div class="subtitle">' + value.artist_name +
                            '</div>' +
                        `<i class="bi playListPlay bi-play-circle-fill" data-id="${value.id}">` +
                        '</i>' +
                        '</h5>' +
                        '</li>'
                    });
                    
                    $('ul.songList').html(songs);
                    songEvent();
                },
                error: function () {
                    alert('Could not get song recommendations for current track');
                }
            });
        })
    })

}