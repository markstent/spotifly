# Spotifly

![Spotifly logo](spotifly.png)

Spotifly  allows users to play short snippets of a playlist in random order. It is designed to provide a quick and easy way to discover new music and playlists without having to listen to full tracks or playlists.

An advantage of Spotifly is its ability to help users discover new music and playlists. By playing short snippets of tracks in random order, the app can expose users to a wide range of artists and genres, allowing them to explore and discover new music that they might not have otherwise encountered.

### Installation

To install the Spotifly module, follow these steps:

 - Clone the repository: [git clone](https://github.com/myusername/spotifly.git)
 - Install the required Python packages: `pip install -r requirements.txt`
 - Set up a Spotify Developer account and create a new [Spotify app](https://developer.spotify.com/documentation/general/guides/app-settings/) - a great article on this can be found [here](https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b)
 - Add your Spotify app credentials to the variable list in use_spotify.py: client_id, client_secret, and redirect_uri
 - Set the playlist_name variable to set the name of the playlist you want to play
 - Import the spotify_player function from the spotifly module
 - Call the play_random_playlist function with the required arguments to start playing snippets from the playlist

Here's an example code snippet:

##### `from spotifly import spotify_player`

Set the required variables

 - USERNAME = 'USERNAME' #obtained from Spotify developer portal
 - USERID = 'USERID' #Spotify user id (from normal Spotify account)
 - PLAYLIST_NAME = 'PLAYLIST_NAME'
 - CLIENT_ID = 'CLIENT_ID' #obtained from Spotify developer portal
 - CLIENT_SECRET = 'CLIENT_SECRET' #obtained from Spotify developer portal
 - REDIRECT_URI = 'REDIRECT_URI' #Make sure this is the same as in your developer portal
 - MIN_PLAY_TIME = 35 #Miniumum playtime for each song in playlist
 - MAX_PLAY_TIME = 60 #Maximum playtime for each song in playlist
 - VOLUME = 80

 #Call the player

 ##### `player = spotify_player(client_id = CLIENT_ID, userid = USERID, client_secret =         CLIENT_SECRET, redirect_uri=REDIRECT_URI,username = USERNAME)`


Set the volume for the playlist to play

##### `player.set_volume(VOLUME)`


Play the playlist in random order

##### `player.play_playlist(PLAYLIST_NAME, MIN_PLAY_TIME, MAX_PLAY_TIME)`


Get a list of all playlists on the users account

##### `print(player.get_playlists())`


Get a list of tracks in a specific playlist

##### `print(player.list_tracks(playlist_name))`

### Contributing
If you want to contribute to the Spotifly module, feel free to submit a pull request or open an issue. Any feedback or suggestions are welcome!

### License
The Spotifly module is licensed under the MIT License. See the [LICENSE](license.txt) file for more information.
