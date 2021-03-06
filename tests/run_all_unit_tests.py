import unittest
import logging 
import ostrawling as ost
import numpy as np 

class TestParticleMethods(unittest.TestCase):
    def test_el_mass(self):
        el = ost.Particle(pdg_id=11, momentum=ost.FourMomentum((1.,1.,1.,1.))) 
        self.assertEqual( el.mass(), 0.5e-3)

    def test_mu_mass(self):
        mu = ost.Particle(pdg_id=13, momentum=ost.FourMomentum((1.,1.,1.,1.))) 
        self.assertEqual(mu.mass(), 106e-3)

class TestFourMomentumMethods(unittest.TestCase):
    def test_p4_addition(self): 
        a = ost.FourMomentum((100,1,1,1),'x,y,z,e')
        b = ost.FourMomentum((50,1,1,1),'x,y,z,e')
        c = a +b 

        self.assertTrue(c.px, a.px + b.px )
        self.assertTrue(c.py, a.py + b.py )
        self.assertTrue(c.pz, a.pz + b.pz )
        self.assertTrue(c.e, a.e + b.e)

    def test_p4_eta_calc(self):
        a = ost.FourMomentum((100,1,1,1),'x,y,z,e')
        eta = .5*np.log( (np.sqrt(100.0**2 +2.0) + 1.)/(np.sqrt(100.0**2 +2.0) - 1.) )
        self.assertTrue(a.eta, eta)
    
    def test_p4_pt_calc(self):
        a = ost.FourMomentum((100,0.0,1,1),'x,y,z,e')
        self.assertTrue(a.pt, 100.0 )
        a = ost.FourMomentum((0.0,100.0,1,1),'x,y,z,e')
        self.assertTrue(a.pt, 100.0 )
        a = ost.FourMomentum((5.0,5.0,1,1),'x,y,z,e')
        self.assertTrue(a.pt, 25.0 )
    
class TestGeneratorMethods(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            foo = ost.Generator(process=None, config={'output_file': 'foo.csv'})

    def test_generating_nevents(self):
        with self.assertRaises(ValueError):
            event_info = {
                's': 2000.0,
                'sqrt_s': np.sqrt(2000.0)
            }
            generator = ost.Generator(process=ost.Dummy(event_info=event_info),
                                      config={'output_file': 'tests/foo.csv'}
                                      )
            generator.generate_n_event('a')

class TestProcessMethods(unittest.TestCase):
    def test_undefined_process(self):
        with self.assertRaises(NotImplementedError):
            ost.create_process('blahlafga')

class TestSaverClass(unittest.TestCase):
    def test_undefined_saver(self):
        with self.assertRaises(NotImplementedError):
            ost.create_saver('foo.txt', '')
        

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.disabled = True
    unittest.main()