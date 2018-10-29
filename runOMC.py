import ostrawling as ost
import logging 
from ostrawling import Generator
from ostrawling import processes 


# 
generator = Generator(process=ost.processes.EEtoMuMu(),
                      saver='csv',
                      config=None,
                      )

generator.generate_n_event(100)

generator.save()


        