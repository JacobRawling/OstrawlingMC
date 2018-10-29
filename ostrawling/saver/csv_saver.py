"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to save generated events to various output files as specified
by the user. 
"""
import logging
from .saver import Saver

class CSVSaver(Saver):

    def open_file(self):
        self.output_file = open(self.output_file, "w")

    def close_file(self):
        self.output_file.close()

    def save_event(self, event, event_number):

        # Read particle by particle
        event_line = "%d, "%event_number
        total = None
        for p in event.final_state_particles:
            if total is None:
                total = p.momentum
            else:
                total = total + p.momentum
            event_line += "%d, %.4g, %.4g, %.4g, %.4g,"%(p.pdg_id, p.momentum.pt,p.momentum.eta, p.momentum.phi, p.momentum.m)
        event_line += "%d, %.4g, %.4g, %.4g, %.4g,"%(-1, total.pt,total.eta, total.phi, total.m)

        # remove the trailing comma
        event_line = event_line[:-1] + '\n'
        self.output_file.write(event_line)



