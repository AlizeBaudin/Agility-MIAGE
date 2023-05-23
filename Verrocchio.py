from typing import List
from Eleve import *
import Splinter
import dataclasses
import Music


class Verrochio:
    def __init__(self, nom: str, date_fondation: int, master: Splinter):
        self.nom = nom
        self.date_fondation = date_fondation
        self.artistes = []
        self.master = master
        self.music = Music
        self.playist = []

    # Getter et Setter
    def get_nom(self) -> str:
        return self.nom

    def set_nom(self, nom: str):
        self.nom = nom

    def get_date_fondation(self) -> int:
        return self.date_fondation

    def set_date_fondation(self, date_fondation: int):
        self.date_fondation = date_fondation

    def get_artistes(self) -> List[Eleve]:
        return self.artistes

    def set_artistes(self, artistes: List[Eleve]):
        self.artistes = artistes

    # Fonctions de la classe
    def ajouter_artiste(self, nom_artiste: Eleve):
        self.artistes.append(nom_artiste)

    def nombre_artistes(self) -> int:
        return len(self.artistes)

    def afficher_artistes(self):
        print("Les artistes travaillant dans l'atelier sont : ")
        for artiste in self.artistes:
            print(artiste)

# ---------------------------------------------------------------------- Partie music
    def ecouter_music(self, music):
        print("Dans l'atelier nous écoutons la musique " + music.getNom())

    def ajouter_music(self, nom_music: Music):
        self.playist.append(nom_music)

    def taille_playist(self) -> int:
        return len(self.playist)


def ajouter_artiste(nom_artiste):
    return nom_artiste


def ecouter_musique(music):
    return ecouter_musique(music)


def ajouter_music(music):
    return music


def taille_playist(playist=None):
    return len(playist)
