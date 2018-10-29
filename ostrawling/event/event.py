
class Event:
    def __init__(self, sqrt_s, final_state_particles):
        self.final_state_particles = final_state_particles
        self.sqrt_s = sqrt_s
        self.weight = 1.0

    def set_weight(self, weight=1.0):
        self.weight = weight

