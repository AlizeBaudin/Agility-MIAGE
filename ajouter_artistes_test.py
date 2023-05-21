from dataclasses import dataclass
from behave import *
from Verrocchio import *


@dataclass
class ManageArtisteInSteps:
    _artiste: Eleve.Eleve
    _master: Splinter
    _atelier: Verrocchio

    def __init__(self):
        self._master = Splinter.getNom(self._master)
        self._atelier = Verrocchio.ajouter_artiste(nom_artiste=self._artiste.getNom())

    @given("un eleve Leonardo")
    def un_eleve_leonard(self):
        self._artiste = Eleve.Eleve("Leonardo", 1452, "Verrocchio", self._master)

    @when("Splinter accueil artiste")
    def ajouter_artiste_atelier(self):
        _master = Splinter.ajoutEleve(self._artiste)

    @then("Leonardo est mon eleve")
    def leonardo_eleve_ajouter(self):
        _atelier = Verrocchio.ajouter_artiste("Leonardo")

    @given("eleve {eleve}")
    def eleve(self, eleve):
        self._artiste=Eleve.Eleve(eleve)

    @then("ajout {eleve}")
    def leonardo_eleve_ajouter(self, eleve):
        _atelier = Verrocchio.ajouter_artiste(eleve)