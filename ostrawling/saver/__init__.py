from .saver import *
from .csv_saver import *
from .hepmc_saver import *

def create_saver(output_file, saver='csv'):
    if saver == 'csv':
        return CSVSaver(output_file)
    if saver == 'hepmc':
        return HepMCSaver(output_file)

    return Saver(output_file)