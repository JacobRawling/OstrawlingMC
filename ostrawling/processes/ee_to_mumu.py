"""

"""
from .process import Process 
import numpy as np

class EEtoMuMu(Process): 
    def __init__(self):
        """
        ToDo: Create some sort of event outline that specifies outparticle masses? ????
        """
        pass

    def integrand(self, phase_space_point):
        """
        ToDo:  code in general formula for 2>2 xsec and given energy Q_0 
        """
        pass  

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
        pass 

    def phase_space_to_event(self, phase_space_point):
        """
        @brief: Converts a point in phase space (which has dimensions equal to
        the true degrees of freedom of the integrand) and returns the four-mom
        enta of the particles of the process.  

        @params
        """
        pass 