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
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)

    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        print(f"Adding song. Song count: {cls.count}")

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            print(f"Adding to genres. Genre list: {cls.genres}")
        else:
            print(f"Duplicate genre. Genre list: {cls.genres}")

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            print(f"Adding to artists. Artist list: {cls.artists}")
        else:
            print(f"Duplicate artist. Artist list: {cls.artists}")


    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genres:
            if genre in cls.genres: 
                genre 
                # increment value of key by 1
            else:
                pass

    @classmethod
    def add_to_artist_count(cls):
        pass


# whatuneed = Song("whatuneed", "Evan Giia", "Vapor Soul")
# tobeyours = Song("tobeyours", "Odesza", "Electronic")
# betternow  = Song("betternow", "Odesza", "Electronic")
