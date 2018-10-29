from .four_momenta import FourMomentum

class Particle:
    def __init__(self, pdg_id, momentum):
        self.pdg_id = pdg_id
        self.momentum = momentum
        self.mass = self.get_mass(pdg_id)

    def get_mass(self, pdg_id):
        return 1.0
