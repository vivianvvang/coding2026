import heapq
from collections import defaultdict

class MusicPlayer:
    def __init__(self):
        self.songs = []
        self.songs_play_counts = {} #total play counts
        self.user_history = {} # user -> played songs
    
    def add_song(self, title):
        song_id = len(self.songs)
        self.songs.append(title)
        self.songs_play_counts[song_id] = 0

        return song_id

    def play_song(self, song_id, user_id):
        if song_id < 0 or song_id >= len(self.songs):
            return
        self.songs_play_counts[song_id] += 1

        if user_id not in self.user_history:
            self.user_history[user_id] = []

        self.user_history[user_id].append(song_id)

        # PART II
        self.user_history[user_id].append(song_id)
        if len(self.user_history[user_id]) > 3:
            self.user_history[user_id].pop(0)

    def print_analytics_summary(self):
        for song_id, count in self.songs_play_counts.items():
            print(song_id, count)
    
    def last_three_played_song_titles(self, user_id):
        history = self.user_history.get(user_id, [])
        return [self.songs[s_id] for s_id in reversed(history)]
    

    def print_top_k_analytics_summary(self, k):
        if k <= 0: 
            return
        for song, count in self.songs_play_counts.items():
            if count > 0:
                flipped_items = [(count, song_id) for song_id, count in self.songs_play_counts.items()]
                top_k_pairs = heapq.nlargest(k, flipped_items)
                for count, song_id in top_k_pairs:
                    if count > 0:
                        print(f"Plays: {count} | Song: '{self.songs[song_id]}'")


player = MusicPlayer()
player.add_song("Song 1")
player.add_song("Song 2")
player.play_song(0,"user1")
player.play_song(1,"user1")
player.play_song(1,"user2")
player.print_analytics_summary()
player.last_three_played_song_titles("user1")
player.print_top_k_analytics_summary(2)