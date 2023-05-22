import dataclasses

import Eleve
import Music
import Verrocchio


class Splinter:
    def __init__(self, nom, anneeNaissance):
        self.nom = nom
        self.anneeNaissance = anneeNaissance
        self.maitreDe = Eleve
        self.atelier = Verrocchio
        self.music = Music

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def ajoutEleve(self, artiste):
        self.atelier.ajouter_artiste(artiste)

    def enCours(self):
        self.maitreDe.apprentissage()

    def ordonne_couleur(self, artiste):
        self.maitreDe.prepare_couleur(artiste)

# ---------------------------------------------------------------------- Partie music
    def fait_decouvrir_musique(self, music):
        self.atelier.ecouter_musique(music.getNom())

def getNom(nom):
    return nom


def ajoutEleve(artiste, atelier=Verrocchio):
    return atelier.ajouter_artiste(artiste)