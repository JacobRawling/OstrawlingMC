"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: Abstract base class for generic process for HEP MC event generator. 
"""

class Process:
    def __init__(self):
        pass

    @abstractmethod
    def integrand(self, event):
        pass

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def draw_phasespace_point(self):
        """
        Draws a point in phase-space ToDo: elaborate 
        """
        pass 

    @abstractmethod 
    def phase_space_to_event(self, phase_space_point):
        """
        @brief: Converts a point in phase space (which has dimensions equal to
        the true degrees of freedom of the integrand) and returns the four-mom
        enta of the particles of the process. 
        """
        pass