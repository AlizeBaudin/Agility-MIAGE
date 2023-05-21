import unittest
import Verrocchio
from Eleve import Eleve
from Splinter import Splinter


class TestConcoursArt(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        pass

    def testAjouterArtiste(self):
        master = Splinter("Splinter", 1435)
        atelier = Verrocchio.Verrochio("Verrochio", 1438, master)
        artiste1 = Eleve("Leonardo da Vinci", 1452, atelier, master)
        # artiste2 = Eleve("Donatello", 1452, atelier, master)
        atelier.ajouter_artiste(artiste1)
        # atelier.ajouter_artiste(artiste2)
        self.assertEqual(1, atelier.nombre_artistes())


if __name__ == '__main__':
    unittest.main()
