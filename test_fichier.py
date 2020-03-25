import unittest
from fichier import prendre_colis, poids_dans_l_ascenceur, creation_colis, creation_colis2, poids_restant_dans_l_ascenceur


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
        self.ascenceur = {"colis": [], "poids_max": 25}
        self.lot = creation_colis2(['enveloppe', 'petit', 'moyen', 'grand','enorme','petit','enveloppe','enorme'])
        self.lot3enormes = creation_colis2(["enorme"] * 3)

    def test_prendre_lot_enorme(self):
        ascenceur = self.ascenceur
        lot3enormes = self.lot3enormes
        prises = [prendre_colis(ascenceur, colis) for colis in lot3enormes]
        self.assertEqual(prises, [True, True, False])
        self.assertEqual(ascenceur["colis"], lot3enormes[:2])
    
    def test_prendre_colis(self):
        ascenceur = self.ascenceur
        lot = self.lot
        prise = [prendre_colis(ascenceur, colis) for colis in lot]
        self.assertEqual(prise, [True, True, True, True, True, True, True, False])   

    def test_poids_dans_l_ascenceur(self):
        ascenceur = self.ascenceur
        lot = self.lot
        prise = [prendre_colis(ascenceur, colis) for colis in lot]
        self.assertEqual(prise, [True, True, True, True, True, True, True, False])
        poids_dans_l_ascenceur(ascenceur)
        self.assertEqual(ascenceur["colis"], lot[:7])

    def test_ship(self):
        categorie, ascenceur, lot = self.categorie, self.ascenceur, self.lot
        a1 = categorie[:7]
        poids = poids_restant_dans_l_ascenceur(ascenceur)
        for categorie in a1:
           prendre_colis(ascenceur, colis)
        restants = categorie[7:]
        prend_colis(restant[0], ascenceur)
        self.assertEquals(ascenceur['colis'], [restant[0]])
       

if __name__ == "__main__":
    import fichier
    import doctest

    doctest.testmod(fichier, verbose=True)
    import unittest

    unittest.main()
