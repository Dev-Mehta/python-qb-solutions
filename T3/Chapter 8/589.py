class Artist:
    def __init__(self,name):
        self.name = name
        self.albums = []
        self.songs = []

    def __str__(self):
        return self.name

class Song:
    def __init__(self, name: str,artist: Artist):
        self.name = name
        self.artist = artist

class Playlist:
    def __init__(self, title: str, songs=[]):
        self.name = title
        self.songs = songs

    def add_song(self, song: Song):
        self.songs.append(song)

class Album:
    def __init__(self, title: str, artist: Artist):
        self.name = title
        self.artist = artist
        self.songs = []

    def add_track(self, track):
        self.songs.append(track)

    def __str__(self) -> str:
        return self.name + ' ' + str(len(self.songs)) + ' songs'
        
the_local_train = Artist("The Local Train")
bombay_bandook = Artist("Bombay Bandook")
anand_bhaskar_collective = Artist("Anand Bhaskar Collective")

cl = Song("Choo Lo", the_local_train)
atk = Song("Aaoge Tum Kabhi", the_local_train)
dm = Song("Dil Mere", the_local_train)
dilnawaz = Song("Dilnawaz", the_local_train)

azad = Song("Azad", bombay_bandook)
skp = Song("Shaakhon ke Patte", bombay_bandook)

mhz = Song("Main Hoon Zameen", anand_bhaskar_collective)
radhe = Song("Radhe", anand_bhaskar_collective)
kanha = Song("Kanha", anand_bhaskar_collective)

akp = Album("Aalas Ka Pedh", the_local_train)
akp.add_track(dm)
akp.add_track(dilnawaz)
akp.add_track(cl)
akp.add_track(dilnawaz)
the_local_train.albums.append(akp)
playlist = Playlist("Dopamine Booster")
playlist.add_song(mhz)
playlist.add_song(azad)
playlist.add_song(atk)

print("Aritst's Albums: ")
for album in the_local_train.albums:
    print(f"- {album}")

print("Playlist: " + playlist.name)
for track in playlist.songs:
    print(f"- {track.name}, {track.artist}")