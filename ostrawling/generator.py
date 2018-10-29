"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to manage MC generation of events 
"""
from .saver import create_saver
from .processes import Process
import logging 
from tqdm import tqdm 

class Generator:
    def __init__(self, process, config, saver='csv'):
        """
        @brief Helper class that performs the integration and Monte Carlo modelling
        of a generic process.  

        @params
        process: A ostrawling.Process class that has a well defined implementation
                 of an arbirtary process
        saver: a string defining the saving output type
        config: [NOT IMPLEMENTED YET] 

        """

        logging.basicConfig(format='[OMC|%(levelname)s] %(message)s', level=logging.DEBUG)
        logging.info('Welcome to OstrawlingMC - a simple educational Monte Carlo')

        self.process = process
        if not isinstance(self.process, Process):
            raise ValueError('process argument of a Generator must be of type Process')

        self.saver = create_saver(config['output_file'], saver)
        self.config = config


    def generate_n_event(self, n):
        """
        @Brief generate n events of process that is set at initalization
        
        @params
        n: integer number of events
        """
        if not isinstance(n, int):
            raise ValueError('Can only generate an integer number of events and parameter n was not an integer!')


        logging.info('Generating %d events.'%n)

        events, total_integral = [], 0.
        for i in tqdm(range(n)):
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

        logging.info('Processed %d events.'%n)
        logging.info(' x-section: %.5g'%self.xsec)
        return self.xsec

    def save(self):
        """
        @Brief calls the open event saver and feeds it one event at a time to save
        """
        for e in self.events:   
            self.saver.save_event(e)



