from .ee_to_mumu import EEtoMuMu
from .dummy import *

def create_process(process, event_info=None):
    if process.lower() == 'dummy':
        return Dummy(event_info)
    elif process.lower() =='eetomumu':
        return EEtoMuMu()
        
    return Process()