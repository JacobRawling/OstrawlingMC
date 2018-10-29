from .four_momentum import FourMomentum

class Particle:
    def __init__(self, pdg_id, momentum):
        self.pdg_id = pdg_id
        self.momentum = momentum
        self.momentum.set_basis(
                (momentum.px(),momentum.py(), momentum.pz(),
                Particle.get_mass(pdg_id)),
                'x,y,z,m'
            ) 

    def mass(self):
        return self.momentum.m()

    @staticmethod
    def get_mass( pdg_id):
        # Electrons
        if abs(pdg_id) == 11:
            return 0.5e-3 
        # Muons 
        if abs(pdg_id) == 13:
            return 106e-3 
        return 1.0
