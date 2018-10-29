"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to manage MC generation of events 
"""

class Generator:
    def __init__(self):
        self.solver = None
        self.processess = None
        self.saver = None
        pass

    def integrate_process(self, event)
        #Something to do with four vectors ???? 

        #

        solver.integrate(process.integrand, event) 



    def generate_n_event(self, n)
        events = []
        for i in range(n):
            # Sample a random event that obeys conservation laws
            trial_event = process.get_random_event() 

            # Integrate the 
            integral = process.integrand(trial_event) 
            total_integral += integral 

            # Store all events
            events.append(trial_event)

        self.xsec = process.get_volume() * total_integral/n
        return self.xsec