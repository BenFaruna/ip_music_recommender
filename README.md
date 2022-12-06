# IP Music Recommender

## INTRODUCTION

* Song recommendations have existed for a long time, but in majority of the scenarios the recommendation is determined after learning the user preferences over a period of time, like looking at his past song preferences, time he listens to the music etc. 

Recommendation system is a filtering system, the purpose of which is to predict the preference that a user would give to a particular element, in our case – to a song. It is a core of huge engines that work by certain recommender algorithms and suggest a single item or a set of items to users based on such predictions.

Whether we are aware of it or not, a variety of recommendation systems have become an integral part of our daily routine since recently. Starting from accurately targeted advertising product suggestions and finishing with personalized video or music playlists compiled specifically for us – recommendation systems seem to be encompassing our everyday lives from literally every corner of digital space

STATISTIC ALGORITHMS
content-based (recommendations based on the similarity of content or, in our case — attributes of two songs)
collaborative (recommendations based on similarity of users’ preferences and using matrices with ratings for each content piece, in our case — a song)
Geographical-base( recommendation base on users loaction and music populaity in a specific area).

### Application Description
IP Music recommender is a music recommendation application that helps users find new songs attuned to their taste and style of music. The application relies on user search and selection to give song recommendations based on current selection. The application allows users to preview songs to get a feel of the songs recommmended and searched. This can help users make sing picks for a new playlist without getting to play songs in full.
The application relies on Spotify's API to function and give recommendation, it is not a music streaming web application, although there is a function to preview songs, it is but a fraction of the actual song.

### Libraries Used 
* Flask
* JQuery
* Spotipy
* Sqlalchemy

* DATABASE: *MySql*
* LANGUAGES: *HTML, CSS, JavaScript, Python*

Checkout the live site on https://ip-music-recommender.onrender.com.

## INSTALLATION
To use this application on your local machine you must have python and MySql database installed on your machine and you need a Spotify developers account, if you don't have one head to https://developer.spotify.com to create an account.

1. Clone the repository onto your local machine and navigate into the folder.

```
$ git clone https://github.com/BenFaruna/ip_music_recommender.git
$ cd ip_music_recommender
ip_music_recommender$
```

2. Using the file [setup_mysql_user.sql](./setup_mysql_user.sql) copy and paste the commands on MySql shell environment to create a database and user.

3. Create a virtual machine (optional) and install the pacages used for the project using pip.
To learn about virtual environments follow this [link](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

On windows (powershell)
```powershell
ip_music_recommender$ $env:SPOTIPY_CLIENT_ID = "<your_client_id>"
ip_music_recommender$ $env:SPOTIPY_CLIENT_SECRET = "<your_client_secret>"
ip_music_recommender$ $env:DATABASE_URL = "mysql+mysqldb://music_dev:music_dev_pwd@localhost/music_dev_db"
```
On linux (shell)
```sh
ip_music_recommender$ SPOTIPY_CLIENT_SECRET="<your_client_id>"
ip_music_recommender$ SPOTIPY_CLIENT_SECRET="<your_client_secret>"
ip_music_recommender$ DATABASE_URL="mysql+mysqldb://music_dev:music_dev_pwd@localhost/music_dev_db"
```
4. Once environmental variables have been added, you can start the application.

```
ip_music_recommender$ python main.py
```
Once that command has been entered the program will be started on localhost port 5000.

On your browser, enter the address http://localhost:5000/home to see the web application.

## USAGE

## CONTRIBUTING

## RELATED PROJECTS

## AUTHORS

Elizabeth W. Salako - [Github](https://github.com/Elisheba12) / [Twitter](https://twitter.com/lisheab) / [LinkedIn]()

Benjamin Faruna Adejo - [Github](https://github.com/BenFaruna) / [Twitter](https://twitter.com/neodynamics) / [LinkedIn](https://www.linkedin.com/in/benjaminfaruna)

Adebayo Idris - [Github](https://github.com/Ade3164) / [Twitter](https://twitter.com/eedrees3?t=xKf3ncU9T-kJsLiFtppP4w&s=09) / [LinkedIn]()
