class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_to_genres(self)
        Song.add_to_artists(self)

        Song.add_song_to_count(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls, self):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, self):
        cls.genres.append(self.genre)

    @classmethod
    def add_to_artists(cls, self):
        cls.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls,self):
        if self.genre not in self.genre_count:
            self.genre_count[self.genre] = 1
        else:
            self.genre_count[self.genre] += 1

    @classmethod
    def add_to_artist_count(cls,self):
        if self.artist not in self.artist_count:
            self.artist_count[self.artist] = 1
        else:
            self.artist_count[self.artist] += 1

