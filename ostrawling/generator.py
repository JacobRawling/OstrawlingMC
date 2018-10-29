"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to manage MC generation of events 
"""

class Generator:
    def __init__(self):
        self.processess = None
        self.saver = None
        pass


    def generate_n_event(self, n):
        events = []
        for i in range(n):
            # Sample a random event that obeys conservation laws
            ps_point = process.draw_phasespace_point() 

            # Integrate the 
            integral = process.integrand(ps_point) 
            total_integral += integral 

            # Store all events
            events.append( process.phase_space_to_event(ps_point) )
            events[-1].set_weight(integral)

        self.events = events
        self.xsec = process.get_volume() * total_integral/n
        return self.xsec

    def save(self):

        
        for e in self.events:   
            self.saver.new_event(e)

