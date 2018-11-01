#!/usr/bin/env python
#coding=utf-8
"""

"""

import ostrawling as ost
import logging 
import numpy as np 
import sys

# 
def main():
    """
    Run the generator on an arbitrary run card. Default run cards can be found 
    in the run_card folder. 

    The structure of arguments for this is as follows: 


    """
     # Read in the arguments and default run card 

    try:
      assert sys.version_info >= (3,0)
    except AssertionError:
      print("\033[1m\033[31;5;31mError:\033[0m Please use python 3. The future is now 😘")
      exit(-1)
    

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