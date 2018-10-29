"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to manage MC generation of events 
"""
from .saver import create_saver
import logging 

class Generator:
    def __init__(self, process, saver='csv', config=None):
        self.process = process
        self.saver = create_saver(saver)
        self.config = config

    def generate_n_event(self, n):
        events, total_integral = [], 0.
        for i in range(n):
            # Sample a random event that obeys conservation laws
            ps_point = self.process.draw_phasespace_point() 

            # Integrate the 
            integral = self.process.integrand(ps_point) 
            total_integral += integral 

            # Store all events
            events.append(self.process.phase_space_to_event(ps_point) )
            events[-1].set_weight(integral)

        self.events = events
        self.xsec = self.process.volume() * total_integral/n
        return self.xsec

    def save(self):
        pass
        # print(self.events)
        # for e in self.events:   
        #     self.saver.new_event(e)

