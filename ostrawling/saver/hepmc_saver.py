"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to save generated events to various output files as specified
by the user. 
"""
import logging
import numpy as np
from .saver import Saver

class HepMCSaver(Saver):

    def open_file(self):
        self.output_file = open(self.output_file, "w")
        
        # Start event listing
        self.output_file.write('HepMC::Version 2.06.09 \n')
        self.output_file.write('HepMC::IO_GenEvent-START_EVENT_LISTING \n')

    def close_file(self):
        # End event listing
        self.output_file.write('HepMC::IO_GenEvent-END_EVENT_LISTING')
        self.output_file.close()


    def save_event(self, event, event_number):

        # WARNING: The following code only works for 2to2 fixed leading order calculations

        event_out = ''

        # General GenEvent information
        event_out += 'E %d -1 -1.0000000000000000e+00 -1.0000000000000000e+00 -1.0000000000000000e+00 0 0 1 10001 10002 0 1 %.17g \n'%(event_number, event.weight)
        # Weight names
        event_out += 'N 1 "Default" \n'
        # Momentum and position units
        event_out += 'U GEV MM \n'

        # Vertex
        event_out += 'V -1 0 0 0 0 0 2 4 0 \n'

        # Read particle by particle


        # Give particles a barcode starting from 10001  
        # for no reason other that's what Herwig does.
        barcode = 10001


        for p in event.initial_state_particles:

            # Use calculated mass to allow for outputting off-shell particles
            calc_mass = np.sqrt(p.momentum.p2+p.momentum.e**2)

            event_out += "P %d %d %.4g %.4g %.4g %.4g %.4g 0 0 -1 0 \n"%(barcode, p.pdg_id, p.momentum.px, p.momentum.py, p.momentum.pz, p.momentum.e, calc_mass)
            barcode += 1

        
        for p in event.final_state_particles:

            calc_mass = np.sqrt(p.momentum.p2+p.momentum.e**2)

            event_out += "P %d %d %.4g %.4g %.4g %.4g %.4g 0 1 0 0 0 0 \n"%(barcode, p.pdg_id, p.momentum.px, p.momentum.py, p.momentum.pz, p.momentum.e, calc_mass)
            barcode += 1

        # write to file
        self.output_file.write(event_out)
