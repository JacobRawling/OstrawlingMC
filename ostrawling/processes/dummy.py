"""

"""
from .process import Process 
import logging 
import numpy as np
from ostrawling.event import Event, Particle, FourMomentum

class Dummy(Process): 
    def __init__(self, event_info):
        """

        """
        self.s = event_info['s']
        self.sqrt_s = event_info['sqrt_s']

    def integrand(self, phase_space_point):
        """
        ToDo:  code in general formula for 2>2 xsec and given energy Q_0 
        """
        return 1.0

    def volume(self):
        """
        Volume element of integration is 4pi cuz it's 2 to 2 scatter. 
        """ 
        return 4*np.pi

    def draw_phasespace_point(self):
        """
        Draws a point in phase-space. In this case we are drawing two numbers 
        one between -1 and 1, and other between 0 and 2pi corresponding to cos(
        theta) and phi respectively 
        """
        return [np.random.uniform(low=0., high=2.0*np.pi), np.random.uniform(low=-1., high=1.0) ]

    def phase_space_to_event(self, phase_space_point):
        """
        @brief: Converts a point in phase space (which has dimensions equal to
        the true degrees of freedom of the integrand) and returns the four-mom
        enta of the particles of the process.  

        @params
        phase_space_point: a random sampling of a point in phase-space
        """
        
        # Fill in the primary muon that is created in spherical polar co-ordinates
        # for ease of integration 
        phi_a, theta_a = phase_space_point[0], np.arccos(phase_space_point[1])
        m = Particle.get_mass(pdg_id=13)
        p = np.sqrt( self.s - m**2 ) 
        a = Particle(pdg_id=13, momentum=FourMomentum(
                (p, theta_a, phi_a,m ),
                'p,theta,phi,m'
                )
            )

        # Now the recoil muon should be back-to-back in the lab-frame
        b = Particle(pdg_id=-13, momentum=FourMomentum(
                (-a.momentum.px ,-a.momentum.py ,-a.momentum.pz ,m ),
                'x,y,z,m'
                )
            )

        # Store these Particles in a more convininet class 
        final_state_particles = [a,b]
        return Event(
            final_state_particles=final_state_particles,
            sqrt_s=np.sqrt(self.s)
            )