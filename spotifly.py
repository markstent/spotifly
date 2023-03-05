import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random
import time

'''
Spotify app must be running in the background before you run this script
Redirect URI in your code must match the redirect URI on your app in the spotify developer site
Spotify developer information can be found at https://developer.spotify.com/
A username needs to be created in the developer documentation
User ID: is your normal spotify userid and can be found on the Spotify account page

'''


class spotify_player:

    def __init__(self, client_id, userid,  client_secret, redirect_uri, username):
        self.client_id = client_id
        self.userid = userid
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.username = username
        self.scope = 'user-library-read user-read-private user-read-email app-remote-control user-modify-playback-state user-modify-playback-state user-modify-playback-state'
        self.token = util.prompt_for_user_token(self.username, self.scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        self.sp = spotipy.Spotify(auth=self.token)
        self.tracks = None    
        
    def set_volume(self, volume):
        
        """
        Summary:

        Sets the volume of the playlist 

        Parameters:

        volume(int): Volume percentage

        Returns:

        None
        
        """
        self.sp.volume(volume)
        
   # def play_track(self, track):
       # self.sp.start_playback(uris=track)
        

        
    def play_playlist(self, playlist_name, min_seconds, max_seconds):
        
        """
        Summary:
        
        Plays the tracks in the playlist for random time periods between min_seconds and max_seconds
        
        playlist_name: The name of the playlist to play
        min_seconds(int): minimum numver of seconds to play
        max_seconds(int): maximim numver of seconds to play
        
        return:
        
        None
        
        """
        
        # Get playlist ID
        playlists = self.sp.user_playlists(self.userid)
        playlist_id = None
        for playlist in playlists['items']:
            if playlist['name'] == playlist_name:
                playlist_id = playlist['id']
                break
        if not playlist_id:
            print(f'Playlist "{playlist_name}" not found.')
            return
        while True:
            # Get tracks in playlist
            tracks = []
            results = self.sp.playlist_tracks(playlist_id)
            tracks += results['items']
            while results['next']:
                results = self.sp.next(results)
                tracks += results['items']
            
            # Shuffle tracks and play each for a random number of seconds
            random.shuffle(tracks)
            for track in tracks:
                track_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                play_seconds = random.randint(min_seconds, max_seconds)
                print(f'Playing "{track_name}" by {artist_name} for {play_seconds} seconds.')
                try:
                    #trk = track['track']['uri']
                    self.sp.start_playback(uris=[track['track']['uri']])
                    #self.play_track([trk])
                    time.sleep(play_seconds)
                except Exception as error:
                    print(error)

        
    def list_tracks(self, playlist_in):
        
        """
        Summary:

        Creates a list of all tracks in a playlist

        Parameters:

        playlist(text): playlist: 

        Returns:

        list of lists: list of tracks in playlist in format [artistname, trackname], returns 0 if playlist not found
        
        """
        
        if not self.tracks:
            playlist_id = None
            playlist_tracks = []
            playlists = self.sp.current_user_playlists()['items']
            for playlist in playlists:
                if playlist['name'] == playlist_in:
                    playlist_id = playlist['id']
                    break
            if not playlist_id:
                return 0

            self.tracks = self.sp.playlist_tracks(playlist_id=playlist_id)['items']
            random.shuffle(self.tracks)

        for track in self.tracks:
            full_list = list((track['track']['artists'][0]['name'], track['track']['name']))
            playlist_tracks.append(full_list)
        
        return playlist_tracks

            
    def get_playlists(self):
        
        """
        Summary:

        Creates a list of all playlists in the user's Spotify account

        Parameters:

        None

        Returns:

        list: list of playlists
        
        """
        
        playlists = self.sp.current_user_playlists()['items']
        playlist_names = [playlist['name'] for playlist in playlists]
        return playlist_names