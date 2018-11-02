#!/usr/bin/env python
"""

"""

import ostrawling.checks
import ostrawling as ost
import logging 
import numpy as np 

# 
def main():
    """
    Run the generator on an arbitrary run card. Default run cards can be found 
    in the run_card folder. 

    The structure of arguments for this is as follows: 


    """
     # Read in the arguments and default run card 

    config, config_data = ost.get_parameters(config_file='run_cards/default_ee_to_mumu.json',
                               description="Generates events for an arbitrary "
                               "processes as defined in the configuration run "
                               "card.",
                               return_data=True
                               )

    generator = ost.Generator(
                          process=config['process'],
                          saver=config['saver'],
                          config=config,
                          )

    generator.generate_n_event(config['n_events'])

    generator.save()


main()