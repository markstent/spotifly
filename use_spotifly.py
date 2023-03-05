from spotifly import spotify_player


# Make sure your Spotify player is open and is playing

# Playlist settings

USERNAME = 'USERNAME' #obtained from Spotify developer portal
USERID = 'USERPD' #Spotify user id (from normal Spotify account)
PLAYLIST_NAME = 'PLAYLIST_NAME'
CLIENT_ID = 'CLIENT_ID' #obtained from Spotify developer portal
CLIENT_SECRET = 'CLIENT_SECRET' #obtained from Spotify developer portal
REDIRECT_URI = 'REDIRECT_URI' #Make sure this is the same as in your developer portal
MIN_PLAY_TIME = 35 #Miniumum playtime for each song in playlist
MAX_PLAY_TIME = 60 #Maximum playtime for each song in playlist
VOLUME = 80 #sets the volume as percent of the maximum volume for your device

player = spotify_player(client_id  =CLIENT_ID,
                       userid = USERID,
                       client_secret = CLIENT_SECRET,
                       redirect_uri=REDIRECT_URI,
                       username = USERNAME)

#print(player.get_playlists()) #lists all playlists

#print(player.list_tracks(playlist_name))   # List all tracks in the playlist

player.set_volume(VOLUME) # Set the initial volume of the player

player.play_playlist(PLAYLIST_NAME, MIN_PLAY_TIME, MAX_PLAY_TIME)
