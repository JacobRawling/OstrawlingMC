import ostrawling as ost
import logging 
import numpy as np 


# 
event_info = {
    's': 2000.0,
    'sqrt_s': np.sqrt(2000.0)
}
generator = ost.Generator(process=ost.processes.Dummy(event_info=event_info),
                      saver='csv',
                      config=None,
                      )

generator.generate_n_event(10000)
generator.save()


        