import unittest
from fichier import prendre_colis,final_colis_poids, creation_colis, creation_colis2

class MyTestCase(unittest.TestCase):
            
    def setUp(self):
        self.categorie = [creation_colis(categorie) for categorie in['enveloppe', 'petit', 'moyen', 'grand', 'enorme', 'petit', 'envloppe', 'enorme']] 
        self.ascenceur = {'categories': [], 'poids_max': 25}
        
    
    def test_prendre_lot_enorme(self):
        ascenceur = {'colis': [], 'poids_max': 25}
        lot3enormes = creation_colis2(['enorme']*3)
        prises = [prendre_colis(ascenceur, colis) for colis in lot3enormes]
        self.assertEqual(prises, [True, True, False])
        self.assertEqual(ascenceur['colis'], lot3enormes[:2])

    def test_prendre_colis(self):
        enveloppe, petit, moyen, grand, enorme, petit, enveloppe, enorme = [
                creation_colis(categorie) for categorie in 
                ['enveloppe', 'petit', 'moyen', 'grand', 'enorme', 'petit', 'envloppe', 'enorme']]
        ascenceur = {'categories': [], 'poids_max': 25}
        self.assertEqual(prendre_colis(ascenceur, enveloppe), True)
        self.assertTrue(prendre_colis(ascenceur, petit))
        self.assertTrue(prendre_colis(ascenceur, moyen))
        self.assertTrue(prendre_colis(ascenceur, grand))
        self.assertTrue(prendre_colis(ascenceur, enorme))
        self.assertTrue(prendre_colis(ascenceur, petit))
        self.assertTrue(prendre_colis(ascenceur, enveloppe))
        self.assertFalse(prendre_colis(ascenceur, enorme), f"Nous ne pouvons pas accepter un colis de cette categorie car le poids du colis est suppérieur au poids libre restant dans l'ascenceur")
    
    def test_final_colis_poids(self):
        enveloppe, petit, moyen, grand, enorme, petit, enveloppe, enorme = [creation_colis(categorie) for categorie in 
                ['enveloppe', 'petit', 'moyen', 'grand', 'enorme', 'petit', 'envloppe', 'enorme']]
        ascenceur = {'categories': [], 'poids_max': 25}
        self.assertEqual(prendre_colis(ascenceur, enveloppe), True)
        self.assertTrue(prendre_colis(ascenceur, petit))
        self.assertTrue(prendre_colis(ascenceur, moyen))
        self.assertTrue(prendre_colis(ascenceur, grand))
        self.assertTrue(prendre_colis(ascenceur, enorme))
        self.assertTrue(prendre_colis(ascenceur, petit))
        self.assertTrue(prendre_colis(ascenceur, enveloppe))
        self.assertFalse(prendre_colis(ascenceur, enorme), f"Nous ne pouvons pas accepter un colis de cette categorie car le poids du colis est suppérieur au poids libre restant dans l'ascenceur")
    
        final_colis_poids(ascenceur)
        self.assertFalse(ascenceur['categories'])

    def test_ship(self):
        categories, ascenceur = self.categorie, self.ascenceur
        a1 = categories[:7]
        for categorie in a1:
            prendre_colis(categorie, ascenceur)
        restants = categorie[7:]
        prend_colis(restant[0], ascenceur)
        self.assertEquals(ascenceur['categories'], [restant[0]])
        
if __name__ == "__main__":
    import fichier
    import doctest
    doctest.testmod(fichier, verbose=True)
    import unittest
    unittest.main()
