class Album:
    def __init__(self):
        self.musicTracks = []

    def addMusicTrack(self, music):
        self.musicTracks.append(music)

    def getMusicTracks(self):
        return self.musicTracks

    def searchMusicTrackByTitle(self, title):
        for music in self.musicTracks:
            if music.getNom() == title:
                return music
        return None

    def playMusicTrackByTitle(self, title):
        musicToPlay = self.searchMusicTrackByTitle(title)
        # Implement logic for playing the music track, if needed.
        return musicToPlay
