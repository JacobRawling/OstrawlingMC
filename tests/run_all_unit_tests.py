import unittest 
import ostrawling as ost
import numpy as np 

class TestParticleMethods(unittest.TestCase):
    def test_el_mass(self):
        el = ost.Particle(pdg_id=11, momentum=None) 
        self.assertEqual( el.mass, 0.5e-3)

    def test_mu_mass(self):
        mu = ost.Particle(pdg_id=13, momentum=None) 
        self.assertEqual(mu.mass, 106e-3)

class TestFourMomentumMethods(unittest.TestCase):
    def test_p4_mass(self):
        with self.assertRaises( ValueError):
            ost.FourMomentum(px=1,py=1,pz=1,m=1,e=1)

    def test_p4_addition(self): 
        a = ost.FourMomentum(px=100,py=1,pz=1,e=1)
        b = ost.FourMomentum(px=50,py=1,pz=1,e=1)
        c = a +b 

        self.assertTrue(c.px(), a.px() + b.px() )
        self.assertTrue(c.py(), a.py() + b.py() )
        self.assertTrue(c.pz(), a.pz() + b.pz() )
        self.assertTrue(c.e(), a.e() + b.e() )

    def test_p4_e_calc(self):
        pass

    def test_p4_eta_calc(self):
        a = ost.FourMomentum(px=100,py=1,pz=1,e=1)
        eta = .5*np.log( (np.sqrt(100.0**2 +2.0) + 1.)/(np.sqrt(100.0**2 +2.0) - 1.) )
        self.assertTrue(a.eta(), eta)
    
    def test_p4_theta_calc(self):
        pass
    
    def test_p4_pt_calc(self):
        pass
    


if __name__ == '__main__':
    unittest.main()