from dataclasses import dataclass
from behave import *

import Music
import Verrocchio
from Verrocchio import *


@dataclass
class ManageArtisteInSteps:
    _artiste: Eleve.Eleve
    _master: Splinter
    _atelier: Verrocchio
    _music: Music

    def __init__(self):
        self._master = Splinter.getNom(self._master)
        self._atelier = Verrocchio.ajouter_artiste(nom_artiste=self._artiste.getNom())
        self._music = Music.getNom()

    @given("une musique Jimi Hendrix")
    def une_musique_hendrix(self):
        self._music = Music.Music("Jimi Hendrix - All Along the Watchtower",1967)

    @when("Splinter fait ecouter musique")
    def music_dans_atelier(self):
        _master = Splinter.fait_decouvrir_musique(self._music)

    @then("Jimi Hendrix est ecouter")
    def hendrix_est_ecoute(self):
        _atelier = Verrocchio.ecouter_musique("Jimi Hendrix - All Along the Watchtower")

    @given("musique {music}")
    def music(self, music):
        self._music = Music.Music(music)

    @then("musique {music}")
    def la_musique_est_ajouter(self, music):
        _atelier = Verrocchio.ajouter_music(music)
