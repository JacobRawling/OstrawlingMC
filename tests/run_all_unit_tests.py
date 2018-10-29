import unittest 
import ostrawling as ost

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestParticleMethods(unittest.TestCase):
    def test_el_mass(self):
        el = ost.Particle(pdg_id=11, momentum=None) 
        self.assertEqual( el.mass, 0.5e-3)

    def test_mu_mass(self):
        mu = ost.Particle(pdg_id=13, momentum=None) 
        self.assertEqual(mu.mass, 106e-3)

if __name__ == '__main__':
    unittest.main()