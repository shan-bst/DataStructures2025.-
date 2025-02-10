# Example 2: Using Linked List to Implement a Music Playlist
class SongNode:
    def __init__(self, song_name):
        self.song_name = song_name
        self.next = None

class MusicPlaylist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name):
        new_song = SongNode(song_name)
        if not self.head:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song

    def show_playlist(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp.song_name)
            temp = temp.next
        return songs

# Demonstrating Music Playlist
playlist = MusicPlaylist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
print("Music Playlist:", playlist.show_playlist())