#!/usr/bin/env python
"""

"""

import ostrawling as ost
import logging 
import numpy as np 


# 
event_info = {
    's': 2000.0,
    'sqrt_s': np.sqrt(2000.0)
}
config = {'output_file': 'out/test.csv'}
generator = ost.Generator(process=ost.processes.Dummy(event_info=event_info),
                      saver='csv',
                      config=config,
                      )

generator.generate_n_event(50000)
generator.save()


        