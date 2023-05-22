import Music


class Eleve:
    Eleve = None

    def __init__(self, nom, anneeNaissance, atelier, master):
        self.nom = nom
        self.anneeNaissance = anneeNaissance
        self.atelier = atelier
        self.master = master
        self.music = Music
        #self.album= Album    #a voir plus tard

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom
        
    def dessiner(self):
        print(self.nom + " dessine dans l'atelier " + self.atelier.getNom())

    def apprentissage(self):
        print(self.nom + " apprend à dessiner dans l'atelier " + self.atelier.getNom())

    def prepare_couleur(self):
        print(self.nom + " prepare a couleur pour "+ self.master.getNom())

 # ---------------------------------------------------------------------- Partie music
    def ecoute_music(self, music):
        print(self.nom + "écoute la music "+ self.music.getNom(music))

    def ecoute_music_atelier(self):
        self.atelier.ecouter_music(self.music)


def apprentissage():
    return apprentissage()

def prepare_couleur(aritist):
    return prepare_couleur(aritist.nom)