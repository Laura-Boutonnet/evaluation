from fichier import categorie

class MyTestCase(unittest.TestCase):
    def test_prendre_colis(self):
        enveloppe, petit, moyen, grand, enorme, petit, enveloppe, enorme = [
                creation_colis(categorie) for categorie in 
                ['enveloppe', 'petit', 'moyen', 'grand', 'enorme', 'petit', 'envloppe', 'enorme']]
        ascenceur = {'categories': [], 'poids_max': 25}
        self.assertEqual(prendre_categorie(ascenceur, enveloppe), True)
        self.assertTrue(prendre_categorie(ascenceur, petit))
        self.assertTrue(prendre_categorie(ascenceur, moyen))
        self.assertTrue(prendre_categorie(ascenceur, grand))
        self.assertTrue(prendre_categorie(ascenceur, enorme))
        self.assertTrue(prendre_categorie(ascenceur, petit))
        self.assertTrue(prendre_categorie(ascenceur, enveloppe))
        self.assertFalse(prendre_categorie(ascenceur, enorme), f"Nous ne pouvons pas accepter un colis de cette categorie car le poids du colis est suppérieur au poids libre restant dans l'ascenceur")
    
    def test_final_colis_poids(self):
        enveloppe, petit, moyen, grand, enorme, petit, enveloppe, enorme = [
                creation_colis(categorie) for categorie in 
                ['enveloppe', 'petit', 'moyen', 'grand', 'enorme', 'petit', 'envloppe', 'enorme']]
        ascenceur = {'categories': [], 'poids_max': 25}
        self.assertEqual(prendre_categorie(ascenceur, enveloppe), True)
        self.assertTrue(prendre_categorie(ascenceur, petit))
        self.assertTrue(prendre_categorie(ascenceur, moyen))
        self.assertTrue(prendre_categorie(ascenceur, grand))
        self.assertTrue(prendre_categorie(ascenceur, enorme))
        self.assertTrue(prendre_categorie(ascenceur, petit))
        self.assertTrue(prendre_categorie(ascenceur, enveloppe))
        self.assertFalse(prendre_categorie(ascenceur, enorme), f"Nous ne pouvons pas accepter un colis de cette categorie car le poids du colis est suppérieur au poids libre restant dans l'ascenceur")
    
        final_colis_poids(ascenceur)
        self.assertFalse(ascenceur['categories'])
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    import unittest
    unittest.main()
