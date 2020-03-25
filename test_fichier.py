import unittest
from fichier import prendre_colis, final_colis_poids, creation_colis, creation_colis2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.categorie = [
            creation_colis(categorie)
            for categorie in [
                "enveloppe",
                "petit",
                "moyen",
                "grand",
                "enorme",
                "petit",
                "envloppe",
                "enorme",
            ]
        ]
        self.ascenceur = {"categories": [], "poids_max": 25}

    def test_prendre_lot_enorme(self):
        ascenceur = {"colis": [], "poids_max": 25}
        lot3enormes = creation_colis2(["enorme"] * 3)
        prises = [prendre_colis(ascenceur, colis) for colis in lot3enormes]
        self.assertEqual(prises, [True, True, False])
        self.assertEqual(ascenceur["colis"], lot3enormes[:2])

    
    def test_prendre_colis(self):
        ascenceur = {'colis': [], 'poids_max': 25}
        lot = creation_colis2(['enveloppe', 'petit', 'moyen', 'grand','enorme','petit','enveloppe','enorme'])
        prise = [prendre_colis(ascenceur, colis) for colis in lot]
        self.assertEqual(prise, [True, True, True, True, True, True, True, False])
        self.assertEqual(ascenceur["colis"], lot[:7])

    def test_final_colis_poids(self):
        ascenceur = {'colis': [], 'poids_max': 25}
        lot = creation_colis2(['enveloppe', 'petit', 'moyen', 'grand','enorme','petit','enveloppe','enorme'])
        prise = [prendre_colis(ascenceur, colis) for colis in lot]
        self.assertEqual(prise, [True, True, True, True, True, True, True, False])

        final_colis_poids(ascenceur)
        self.assertFalse(ascenceur['categories'])
"""
    def test_ship(self):
        categories, ascenceur = self.categorie, self.ascenceur
        a1 = categories[:7]
        for categorie in a1:
            prendre_colis(categorie, ascenceur)
        restants = categorie[7:]
        prend_colis(restant[0], ascenceur)
        self.assertEquals(ascenceur['categories'], [restant[0]])
       """


if __name__ == "__main__":
    import fichier
    import doctest

    doctest.testmod(fichier, verbose=True)
    import unittest

    unittest.main()
