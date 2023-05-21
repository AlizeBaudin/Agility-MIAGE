import dataclasses

import Verrocchio


class Splinter:
    def __init__(self, nom, anneeNaissance):
        self.nom = nom
        self.anneeNaissance = anneeNaissance
        self.maitreDe = None
        self.atelier = None

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def ajoutEleve(self, artiste):
        self.atelier.ajouter_artiste(artiste)

    def enCours(self):
        self.maitreDe.apprentissage()


def getNom(nom):
    return nom


def ajoutEleve(artiste, atelier=Verrocchio):
    return atelier.ajouter_artiste(artiste)