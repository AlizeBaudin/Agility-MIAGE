import unittest
import Verrocchio
from Eleve import Eleve
from Music import Music
from Splinter import Splinter


class TestAjoutMusic(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        pass

    def testAjouterMusic(self):
        master = Splinter("Splinter", 1435)
        atelier = Verrocchio.Verrochio("Verrochio", 2022, master)
        artiste1 = Eleve("Leonardo da Vinci", 1452, atelier, master)
        atelier.ajouter_artiste(artiste1)
        music1 = Music("Jimi Hendrix - All Along the Watchtower", 1967)
        #atelier.ecouter_music(music1)
        atelier.ajouter_music(music1)
        self.assertEqual(1, atelier.taille_playist())


if __name__ == '__main__':
    unittest.main()
