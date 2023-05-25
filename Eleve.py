import Music


class Eleve:
    Eleve = None

    def __init__(self, nom, anneeNaissance, atelier, master):
        self.nom = nom
        self.anneeNaissance = anneeNaissance
        self.atelier = atelier
        self.master = master
        self.music = Music
        #self.album= Album    

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom
        
    def dessiner(self):
        return self.nom + " dessine dans l'atelier " + self.atelier.getNom()

    def apprentissage(self):
        return self.nom + " apprend à dessiner dans l'atelier " + self.atelier.getNom()

    def prepare_couleur(self):
        return self.nom + " prepare a couleur pour "+ self.master.getNom()

 # ---------------------------------------------------------------------- Partie music
    def ecoute_music(self, music):
        return self.nom + "écoute la music "+ self.music.getNom(music)

    def ecoute_music_atelier(self):
        self.atelier.ecouter_music(self.music)


def apprentissage():
    return apprentissage()

def prepare_couleur(aritist):
    return prepare_couleur(aritist.nom)
