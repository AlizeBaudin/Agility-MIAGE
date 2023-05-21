import Music


class Award:
    def __init__(self):
        self.year = 0
        self.name = ""
        self.music = Music

    def howManyYearsAfterAward(self):
        if self.music is not None:
            return self.music.howOldAreYou(self.music.getEdition()) - (self.year - self.music.getEdition())
        else:
            return 0

    def getMusic(self):
        return self.music

    def setMusic(self, music):
        self.music = music

    def setYear(self, year):
        self.year = year
