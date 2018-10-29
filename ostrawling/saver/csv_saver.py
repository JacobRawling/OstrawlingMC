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
        for p in event.final_state_particles:
            event_line += "%d, %.4g, %.4g, %.4g, %.4g,"%(p.pdg_id, p.momentum.px(),p.momentum.py(), p.momentum.pz(), p.momentum.m())

        # remove the trailing comma
        event_line = event_line[:-1] + '\n'
        self.output_file.write(event_line)



