import Album


class Music:

    def __init__(self, nom, edition):
        self.nom = nom
        self.edition = edition
        self.worstSongAwards = Album

    def howOldAreYou(self):
        return 2023 - self.edition

    def validateEdition(self, edition):
        if edition < 0 or edition > 2023:
            raise ValueError("Invalid edition year.")

    def toSting(self):
        return "The music " + self.nom + " came out in " + str(self.edition)

    def getEdition(self):
        return self.edition

    def setEdition(self, e):
        self.edition = e

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getWorstSongAwards(self):
        return self.worstSongAwards

    def setWorstSongAwards(self, worstSongAwards):
        self.worstSongAwards = worstSongAwards


def getNom(nom):
    return nom

def howOldAreYou(edition):
    return 2023 - edition

def getEdition():
    return getEdition()